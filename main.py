from Paladino import Paladino
from Cavaleiro import Cavaleiro
import random

from Mago import Mago

#função para escolha do personagem
def escolher_personagem():
    print("SELEÇÃO DE PERSONAGEM")
    print("1. Cavaleiro")
    print("2. Paladino")
    print("3. Mago")
#laço de repetição para seleção
    while True:
        opcao = input("\nEscolha o seu personagem")
        nome = input("Digite o nome do seu personagem")

        if opcao == "1":
            return Cavaleiro(nome)

        elif opcao == "2":
            return Paladino(nome)

        elif opcao == "3":
            return Mago(nome)
        else:
            print("Opção incorreta! Escolha 1,2 ou 3.")

def main():
    jogador = escolher_personagem()
    print(f"\n{jogador.nome} seu personagem foi selecionado!")

    jogador.experiencia_ganha()
    jogador.distruicao()

    print("\nStatus das Habilidades")
    print(f"Ataque: {jogador.stats.getAtaque()}")
    print(f"Defesa: {jogador.stats.getDefesa()}")
    print(f"Vida: {jogador.stats.getVida()}")

if __name__ == "__main__":

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

cavaleiro = Cavaleiro("Cavaleiro")

cavaleiro.experiencia_ganha(3)
cavaleiro.distruicao()
print(cavaleiro.stats.getAtaque(), cavaleiro.stats.getDefesa(), cavaleiro.stats.getVida())