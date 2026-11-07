import random
from Mago import Mago
from Stats import Stats
from Paladino import Paladino

def rolar_d20_e_calcular_dano(dano_base: float, personagem) -> tuple[int, str]:
    """
    Rola um dado de 20 lados (d20) e calcula o dano escalonado:
    - 1: Falha crítica (0 de dano)
    - 20: Acerto crítico (Dobro do dano)
    - 2 a 19: Dano proporcional ao resultado (mais perto de 20 = mais dano)
    """
    d20 = 0
    if personagem.azarado:
        for i in range(2):
            temporario = random.randint(1, 20)
            if temporario < d20 or i == 0:
                d20 = temporario
        personagem.azarado = False
    elif personagem.sortudo:
        for i in range(2):
            temporario = random.randint(1, 20)
            if temporario > d20 or i == 0:
                d20 = temporario
        personagem.sortudo = False
    else:
        d20 = random.randint(1, 20)

    if d20 == 1:
        return 0, f"Rolou {d20}: ERRO CRÍTICO! Nenhum dano causado."
    elif d20 == 20:
        dano_final = int(dano_base * 2)
        return dano_final, f"Rolou {d20}: ACERTO CRÍTICO! Dano dobrado ({dano_final})."
    else:
        # Multiplicador proporcional (ex: 10 no dado = 100% do dano base; 15 = 150%; 5 = 50%)
        multiplicador = d20 / 10.0
        dano_final = max(1, int(dano_base * multiplicador))
        return dano_final, f"Rolou {d20}: Dano escalonado obtido ({dano_final})."


class BatalhaManager:
    """Classe responsável pelo fluxo de combate (cumpre o requisito de método/atributo privado do PDF)"""


    def __init__(self, heroi, monstro):
        self.heroi = heroi
        self.monstro = monstro
        self.__turno_atual = 1 # Atributo privado
        self.vida_atual_heroi = self.heroi.stats.getVida()
        self.vida_atual_monstro = self.monstro.stats.getVida()

    def __verificar_vencedor(self):  # Método privado
        if self.vida_atual_heroi <= 0:
            return self.monstro
        elif self.vida_atual_monstro <= 0:
            return self.heroi
        return None
    def ataque_heroi(self, dano_h, defesa_i):
        dano_calculado, msg_dado = rolar_d20_e_calcular_dano(dano_h + self.heroi.stats.getAtaque(), self.heroi)
        dano_real = max(0, dano_calculado - defesa_i)
        self.vida_atual_monstro -= dano_real
        print(f"{self.heroi.nome} atacou! {msg_dado} Dano aplicado ao inimigo: {dano_real}")
    def cura_heroi(self, cura_h):
        self.vida_atual_heroi += cura_h
        print(f"{self.heroi.nome} recuperou {cura_h} de vida.")
    def ataque_inimigo(self, dano_i, defesa_h):
        dano_calculado, msg_dado = rolar_d20_e_calcular_dano(dano_i + self.monstro.stats.getAtaque(),
                                                 self.monstro)
        if isinstance(self.heroi, Paladino):
            if self.heroi.vida_emergencial and self.heroi.vida_extra >= 0:
                dano_real = max(0, dano_calculado - (self.heroi.stats.getDefesa() + defesa_h))
                self.heroi.vida_extra -= dano_real
                print(f"{self.monstro.nome} atacou! {msg_dado} Dano aplicado ao heroi: {dano_real}")
                if self.heroi.vida_extra <= 0:
                    self.vida_atual_heroi += self.heroi.vida_extra
                    self.heroi.vida_emergencial = False
                    self.heroi.carregamento_habilidade = 3
                return
        dano_real = max(0, dano_calculado - (self.heroi.stats.getDefesa() + defesa_h))
        self.vida_atual_heroi -= dano_real
        print(f"{self.monstro.nome} atacou! {msg_dado} Dano aplicado ao heroi: {dano_real}")
        if isinstance(self.heroi, Mago):
            if self.heroi.escudo_imperfeito:
                self.vida_atual_monstro -= (dano_real / 2)
                print("Dano rebatido")
                self.heroi.escudo_imperfeito = False


    def cura_inimigo(self, cura_i):
        self.vida_atual_monstro += cura_i
        print(f"{self.monstro.nome} recuperou {cura_i} de vida.")


    def executar_turno(self):
        while True:
            print(f"\n--- TURNO {self.__turno_atual} ---")

            self.heroi.usar_habilidade_ativa(self.monstro)
            acao_heroi = self.heroi.escolher_acao()
            acao_monstro = self.monstro.escolher_acao()
            dano_h, defesa_h, cura_h, debuff_h = self.heroi.acoes(acao_heroi, self.monstro)
            dano_i, defesa_i, cura_i, debuff_i = self.monstro.acoes(acao_monstro, self.heroi)

            if self.heroi.prioridade == self.monstro.prioridade:
                aleatorio = random.randint(1, 2)
                if aleatorio == 1:
                    if dano_h > 0:
                        self.ataque_heroi(dano_h, self.monstro.stats.getDefesa())
                    if cura_h > 0:
                        self.cura_heroi(cura_h)
                    if dano_i > 0 and not self.monstro.paralisado and self.vida_atual_monstro > 0:
                        self.ataque_inimigo(dano_i, defesa_h)
                    if cura_i > 0 and not self.monstro.paralisado and self.vida_atual_monstro > 0:
                        self.cura_inimigo(cura_i)
                else:
                    if dano_i > 0 and not self.monstro.paralisado:
                        self.ataque_inimigo(dano_i, defesa_h)
                    if cura_i > 0 and not self.monstro.paralisado:
                        self.cura_inimigo(cura_i)
                    if dano_h > 0:
                        self.ataque_heroi(dano_h, self.monstro.stats.getDefesa())
                    if cura_h > 0:
                        self.cura_heroi(cura_h)

            elif self.heroi.prioridade < self.monstro.prioridade:
                if dano_i > 0 and not self.monstro.paralisado:
                    self.ataque_inimigo(dano_i, defesa_h)
                if cura_i > 0 and not self.monstro.paralisado:
                    self.cura_inimigo(cura_i)
                if dano_h > 0:
                    self.ataque_heroi(dano_h, self.monstro.stats.getDefesa())
                if cura_h > 0:
                    self.cura_heroi(cura_h)

            elif self.heroi.prioridade > self.monstro.prioridade:
                if dano_h > 0:
                    self.ataque_heroi(dano_h, self.monstro.stats.getDefesa())
                if cura_h > 0:
                    self.cura_heroi(cura_h)
                if dano_i > 0 and not self.monstro.paralisado and self.vida_atual_monstro > 0:
                    self.ataque_inimigo(dano_i, defesa_h)
                if cura_i > 0 and not self.monstro.paralisado and self.vida_atual_monstro > 0:
                    self.cura_inimigo(cura_i)

            vencedor = self.__verificar_vencedor()
            if vencedor:
                print(f"\nBatalha Encerrada! Vencedor: {vencedor.nome}")
                return vencedor

            self.__turno_atual += 1
            print(f"Vida atual cavaleiro: {self.vida_atual_heroi}")
            print(f"Vida atual goblin: {self.vida_atual_monstro}")
            self.monstro.paralisado = False