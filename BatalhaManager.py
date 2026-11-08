"""Organiza a luta e decide o que acontece em cada turno."""

import random
from Mago import Mago
from Stats import Stats
from Paladino import Paladino
import math
from Inimigos import Tyranid, Nurgle


def rolar_d20_e_calcular_dano(dano_base: float, personagem) -> tuple[int, str]:
    """
    Rola um dado de 20 lados (d20) e calcula o dano escalonado:
    - 1: Falha crítica (0 de dano)
    - 20: Acerto crítico (Dobro do dano)
    - 2 a 19: Dano proporcional ao resultado (mais perto de 20 = mais dano)
    """
    # Primeiro escolhe o resultado do dado, respeitando habilidades de sorte ou azar.
    d20 = 0
    if personagem.azarado:
        for i in range(2):
            temporario = random.randint(1, 20)
            if temporario < d20 or i == 0:
                d20 = temporario
        personagem.azarado = False
    elif isinstance(personagem, Tyranid):
        if personagem.instinto_colmeia:
            # O instinto do Tyranid faz ele ficar com o maior de dois resultados.
            for i in range(2):
                temporario = random.randint(1, 20)
                if temporario > d20 or i == 0:
                    d20 = temporario
            personagem.duracao_instinto_colmeia -= 1
    elif personagem.sortudo:
        # A sorte também deixa o personagem escolher o maior de dois dados.
        for i in range(2):
            temporario = random.randint(1, 20)
            if temporario > d20 or i == 0:
                d20 = temporario
        personagem.sortudo = False
    else:
        d20 = random.randint(1, 20)

    if d20 == 1:
        # Tirar 1 significa que o ataque falhou completamente.
        return 0, f"Rolou {d20}: ERRO CRÍTICO! Nenhum dano causado."
    elif d20 == 20:
        # Tirar 20 dobra o dano calculado.
        dano_final = int(dano_base * 2)
        return dano_final, f"Rolou {d20}: ACERTO CRÍTICO! Dano dobrado ({dano_final})."
    else:
        # Multiplicador proporcional (ex: 10 no dado = 100% do dano base; 15 = 150%; 5 = 50%)
        multiplicador = d20 / 10.0
        dano_final = max(1, int(dano_base * multiplicador))
        return dano_final, f"Rolou {d20}: Dano escalonado obtido ({dano_final})."


class BatalhaManager:
    """Guarda os lutadores e cuida das regras da batalha."""


    def __init__(self, heroi, monstro):
        # Guarda quem está lutando e começa com a vida das fichas.
        # A vida atual da batalha pode mudar sem alterar a vida máxima.
        self.heroi = heroi
        self.monstro = monstro
        self.__turno_atual = 1 # Atributo privado
        self.vida_atual_heroi = self.heroi.stats.getVida()
        self.vida_atual_monstro = self.monstro.stats.getVida()

    def __verificar_vencedor(self):  # Método privado
        # Se a vida de alguém chegou a zero, o outro lutador venceu.
        if self.vida_atual_heroi <= 0:
            return self.monstro
        elif self.vida_atual_monstro <= 0:
            return self.heroi
        return None

    def ataque_heroi(self, dano_h, defesa_i, debuff_ataque_i, debuff_defesa_h):
        # Soma o poder do golpe ao ataque do herói e aplica o efeito do inimigo.
        dano_calculado, msg_dado = rolar_d20_e_calcular_dano(dano_h + self.heroi.stats.getAtaque() - debuff_ataque_i, self.heroi)
        # A defesa do monstro reduz o golpe; o dano nunca fica abaixo de zero.
        dano_real = max(0, dano_calculado - (self.monstro.stats.getDefesa() + defesa_i - debuff_defesa_h))
        self.vida_atual_monstro -= dano_real
        # Guarda o dano para habilidades que precisam saber quanto foi perdido.
        print(f"{self.heroi.nome} atacou! {msg_dado} Dano aplicado ao inimigo: {dano_real}")
        self.monstro.vida_perdida = dano_real

    def cura_heroi(self, cura_h):
        # Soma a cura à vida atual do herói e conta ao jogador.
        self.vida_atual_heroi += cura_h
        print(f"{self.heroi.nome} recuperou {cura_h} de vida.")

    def ataque_inimigo(self, dano_i, defesa_h, debuff_ataque_h, debuff_defesa_i):
        # Calcula o golpe do inimigo usando seu ataque e os efeitos do herói.
        dano_calculado, msg_dado = rolar_d20_e_calcular_dano(dano_i + self.monstro.stats.getAtaque() - debuff_ataque_h,
                                                 self.monstro)
        if isinstance(self.heroi, Paladino):
            if self.heroi.vida_emergencial and self.heroi.vida_extra >= 0:
                # Enquanto Vida Emergencial está ativa, o golpe gasta a vida extra primeiro.
                dano_real = max(0, dano_calculado - (self.heroi.stats.getDefesa() + defesa_h - debuff_defesa_i))
                self.heroi.vida_extra -= dano_real
                print(f"{self.monstro.nome} atacou! {msg_dado} Dano aplicado ao heroi: {dano_real}")
                self.heroi.vida_perdida = dano_real
                if self.heroi.vida_extra <= 0:
                    # O que passar da reserva temporária é descontado da vida normal.
                    self.vida_atual_heroi += self.heroi.vida_extra
                    self.heroi.vida_emergencial = False
                    self.heroi.carregamento_habilidade = 3
                return
        # Se não houver vida extra, a defesa normal do herói diminui o golpe.
        dano_real = max(0, dano_calculado - (self.heroi.stats.getDefesa() + defesa_h - debuff_defesa_i))
        self.vida_atual_heroi -= dano_real
        print(f"{self.monstro.nome} atacou! {msg_dado} Dano aplicado ao heroi: {dano_real}")
        self.heroi.vida_perdida = dano_real
        if isinstance(self.heroi, Mago):
            if self.heroi.escudo_imperfeito:
                # O escudo do Mago rebate metade do dano e se desativa após o golpe.
                self.vida_atual_monstro -= (dano_real / 2)
                print("Dano rebatido")
                self.heroi.escudo_imperfeito = False


    def cura_inimigo(self, cura_i):
        # Soma a cura à vida do monstro.
        self.vida_atual_monstro += cura_i
        print(f"{self.monstro.nome} recuperou {cura_i} de vida.")


    def executar_turno(self):
        # A luta repete turnos até alguém ficar sem vida.
        while True:
            print(f"\n--- TURNO {self.__turno_atual} ---")

            # Primeiro cada lutador prepara suas habilidades e escolhe sua ação.
            self.heroi.usar_habilidade_ativa(self.monstro)
            acao_heroi = self.heroi.escolher_acao()
            acao_monstro = self.monstro.escolher_acao()
            dano_h, defesa_h, cura_h, debuff_ataque_h, debuff_defesa_h = self.heroi.acoes(acao_heroi, self.monstro)
            dano_i, defesa_i, cura_i, debuff_ataque_i, debuff_defesa_i = self.monstro.acoes(acao_monstro, self.heroi)

            # O monstro também pode ativar seu poder antes das ações do turno.
            self.monstro.usar_habilidade_ativa(self.heroi)
            if isinstance(self.monstro, Nurgle):
                if self.monstro.apodrecimento:
                    if self.monstro.carregamento_habilidade == 3:
                        self.monstro.apodrecimento = False
                    # Aplica as penalidades do apodrecimento aos cálculos deste turno.
                    debuff_defesa_i += 7
                    debuff_ataque_i += 7

            # Prioridade decide quem age primeiro; em empate, um dado escolhe.
            if self.heroi.prioridade == self.monstro.prioridade:
                aleatorio = random.randint(1, 2)
                if aleatorio == 1:
                    # O herói age primeiro. Depois o monstro só age se ainda puder.
                    if dano_h > 0:
                        self.ataque_heroi(dano_h, defesa_i, debuff_ataque_i, debuff_defesa_h)
                    if cura_h > 0:
                        self.cura_heroi(cura_h)
                    if dano_i > 0 and not self.monstro.paralisado and self.vida_atual_monstro > 0:
                        self.ataque_inimigo(dano_i, defesa_h, debuff_ataque_h, debuff_defesa_i)
                    if cura_i > 0 and not self.monstro.paralisado and self.vida_atual_monstro > 0:
                        self.cura_inimigo(cura_i)
                    if isinstance(self.monstro, Nurgle):
                        if self.monstro.vida_perdida > 0 and self.monstro.apodrecimento:
                            # O poder de Nurgle também tira vida do herói quando ele é atingido.
                            self.vida_atual_heroi -= 10
                else:
                    # Neste empate, o monstro age primeiro.
                    if dano_i > 0 and not self.monstro.paralisado:
                        self.ataque_inimigo(dano_i, defesa_h, debuff_ataque_h, debuff_defesa_i)
                    if cura_i > 0 and not self.monstro.paralisado:
                        self.cura_inimigo(cura_i)
                    if dano_h > 0:
                        self.ataque_heroi(dano_h, defesa_i, debuff_ataque_i, debuff_defesa_h)
                    if cura_h > 0:
                        self.cura_heroi(cura_h)
                    if isinstance(self.heroi, Paladino):
                        if self.heroi.recuperacao_vida:
                            # Depois de receber o golpe, o Paladino recupera metade do dano.
                            self.vida_atual_heroi += math.ceil(self.heroi.vida_perdida / 2)
                            self.vida_atual_heroi = min(self.vida_atual_heroi, self.heroi.stats.getVida())
                            print(f"{self.heroi.nome} recuperou {self.heroi.vida_perdida / 2} de vida.")
                            self.heroi.recuperacao_vida = False

            elif self.heroi.prioridade < self.monstro.prioridade:
                # O número menor de prioridade faz o herói agir depois do monstro.
                if dano_i > 0 and not self.monstro.paralisado:
                    self.ataque_inimigo(dano_i, defesa_h, debuff_ataque_h, debuff_defesa_i)
                if cura_i > 0 and not self.monstro.paralisado:
                    self.cura_inimigo(cura_i)
                if dano_h > 0:
                    self.ataque_heroi(dano_h, defesa_i, debuff_ataque_i, debuff_defesa_h)
                if cura_h > 0:
                    self.cura_heroi(cura_h)
                if isinstance(self.heroi, Paladino):
                    if self.heroi.recuperacao_vida:
                        # A cura do Paladino acontece depois que o inimigo o atinge.
                        self.vida_atual_heroi += math.ceil(self.heroi.vida_perdida / 2)
                        self.vida_atual_heroi = min(self.vida_atual_heroi, self.heroi.stats.getVida())
                        print(f"{self.heroi.nome} recuperou {self.heroi.vida_perdida / 2} de vida.")
                        self.heroi.recuperacao_vida = False

            elif self.heroi.prioridade > self.monstro.prioridade:
                # O número maior de prioridade faz o herói agir antes do monstro.
                if dano_h > 0:
                    self.ataque_heroi(dano_h, defesa_i, debuff_ataque_i, debuff_defesa_h)
                if cura_h > 0:
                    self.cura_heroi(cura_h)
                if dano_i > 0 and not self.monstro.paralisado and self.vida_atual_monstro > 0:
                    self.ataque_inimigo(dano_i, defesa_h, debuff_ataque_h, debuff_defesa_i)
                if cura_i > 0 and not self.monstro.paralisado and self.vida_atual_monstro > 0:
                    self.cura_inimigo(cura_i)
                if isinstance(self.monstro, Nurgle):
                    if self.monstro.vida_perdida > 0 and self.monstro.apodrecimento:
                        # Se Nurgle foi ferido enquanto apodrecia, também causa dano extra.
                        self.vida_atual_heroi -= 10

            # Depois das ações, confere se a batalha já terminou.
            vencedor = self.__verificar_vencedor()
            if vencedor:
                print(f"\nBatalha Encerrada! Vencedor: {vencedor.nome}")
                return vencedor

            # Mostra a vida dos dois e prepara as variáveis para o próximo turno.
            self.__turno_atual += 1
            print(f"Vida atual {self.heroi.nome}: {self.vida_atual_heroi}")
            print(f"Vida atual {self.monstro.nome}: {self.vida_atual_monstro}")
            self.monstro.paralisado = False
            self.heroi.vida_perdida = 0
            self.monstro.vida_perdida = 0