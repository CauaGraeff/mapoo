from Paladino import Paladino
from Cavaleiro import Cavaleiro
import random

from Mago import Mago

"""
def calcular_ataque(atacante, defensor):
    # 1. Rola o dado
    dado = random.randint(1, 6)

    # 2. Calcula o dano bruto (Dado + Ataque)
    dano_bruto = dado + atacante.ataque

    # 3. Subtrai a defesa do defensor
    dano_final = dano_bruto - defensor.defesa

    # 4. Garante o dano mínimo de 1 (para o ataque nunca ser inútil)
    if dano_final < 1:
        dano_final = 1

    return dano_final
"""

cavaleiro = Paladino("Cavaleiro")
mago = Mago("Mago")
print(cavaleiro.stats.getAtaque())
escolha = cavaleiro.escolher_acao()
print(cavaleiro.acoes(escolha, mago))
