import random

def rolar_d20_e_calcular_dano(dano_base: float) -> tuple[int, str]:
    """
    Rola um dado de 20 lados (d20) e calcula o dano escalonado:
    - 1: Falha crítica (0 de dano)
    - 20: Acerto crítico (Dobro do dano)
    - 2 a 19: Dano proporcional ao resultado (mais perto de 20 = mais dano)
    """
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

    def _init_(self, heroi, monstro):
        self.heroi = heroi
        self.monstro = monstro
        self.__turno_atual = 1  # Atributo privado

    def __verificar_vencedor(self):  # Método privado
        if self.heroi.stats.vida <= 0:
            return self.monstro
        elif self.monstro.stats.vida <= 0:
            return self.heroi
        return None

    def executar_turno(self):
        print(f"\n--- TURNO {self.__turno_atual} ---")

        # 1. Escolha de ações
        acao_heroi = self.heroi.escolher_acao()
        dano_h, defesa_h, cura_h, debuff_h = self.heroi.acoes(acao_heroi, self.monstro)

        # 2. Execução do ataque com rolagem do d20
        if dano_h > 0:
            dano_calculado, msg_dado = rolar_d20_e_calcular_dano(dano_h + self.heroi.stats.ataque)
            dano_real = max(0, dano_calculado - self.monstro.stats.defesa)
            self.monstro.stats.vida -= dano_real
            print(f"{self.heroi.nome} atacou! {msg_dado} Dano aplicado ao inimigo: {dano_real}")

        if cura_h > 0:
            self.heroi.stats.vida += cura_h
            print(f"{self.heroi.nome} recuperou {cura_h} de vida.")

        # 3. Checagem de vencedor
        vencedor = self.__verificar_vencedor()
        if vencedor:
            print(f"\nBatalha Encerrada! Vencedor: {vencedor.nome}")
            return vencedor

        self.__turno_atual += 1
        return None