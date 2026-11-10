"""Mostra as informações dos heróis e deixa escolher um para jogar."""

import random
import sys
from BatalhaManager import BatalhaManager
from Inimigos import Goblin, Orc, Tyranid, Nurgle
from Paladino import Paladino
from Cavaleiro import Cavaleiro
from Mago import Mago

#função de visualização das habilidades de cada personagem
def exibir_menu_detalhado():
    # Explica ao jogador como cada herói funciona.
    print("\n          PAINEL DE HABILIDADE DE CADA PERSONAGEM\n")
#CAVALEIRO
    print("1 - Cavaleiro")
    print("Foco: O Cavaleiro é focado em alta sobrevivência e controle dos dados do adversário.")
    print("Atributos:"
          "\nVida: 12"
          "\nAtaque: 6"
          "\nDefesa: 10")
    print("Habilidade: "
          "\nO Azarão: O inimigo, em vez de rolar um dado, deve rolar dois e obrigatoriamente usar o de menor valor."
          "\nRestrição: Tempo de Recarga de 3 turnos após o uso.")
    print("Ações:"
          "\nCorte Rápido: Ataque padrão. Causa dano."
          "\nDefesa Sólida: Entra em postura defensiva. Recebe defesa neste turno e no próximo, mas fica impossibilitado de atacar por 2 turnos")

#MAGO
    print("2 - Mago")
    print("Foco: O Mago possui baixa sobrevivência, mas tem alto dano e grande versatilidade mágica.")
    print("Atributos:"
          "\nVida: 7"
          "\nAtaque: 10"
          "\nDefesa: 5")
    print("Regra de Habilidades: O Mago só pode escolher e usar uma de suas três habilidades a cada 2 turnos.")
    print("Habilidades:")
    print("\nRaio Paralisante: O inimigo fica paralisado e não pode atacar neste turno."
          "\nDouble Luck: O Mago rola dois dados e pega o maior valor. Efeito dura por 2 turnos."
          "\nEscudo Imperfeito: Ativa um escudo mágico. Rebate 50% do dano recebido de volta para o atacante.")
    print("Ações:"
          "\nBola de Fogo: Ataque padrão. Causa dano."
          "\nSuper Bola de Fogo: Requer 2 turnos para recarga."
          "\nNo segundo turno, causa o dano padrão + 8 de bônus.")

#PALADINO
    print("3 - Paladino")
    print("Foco: O Paladino equilibra ataque e defesa com mecânicas de sustentação e manipulação de vida.")
    print("Atributos:"
          "\nVida: 8"
          "\nAtaque: 7"
          "\nDefesa: 8")
    print("Habilidade:"
          "Vida Emergencial: Aumenta a vida máxima atual temporariamente em por 2 turnos. Tempo de recarga de 3 turnos após o fim do efeito.")
    print("Ações:"
          "\nRecuperação de Vida: O Paladino se expõe para receber o dano do inimigo neste turno e, logo em seguida, cura uma parte da vida perdida."
          "\nCorte Prejudicial: Golpe de ataque. Além de causar dano, reduz o Atributo de Ataque do inimigo.")

#função para escolha do personagem
def escolher_personagem():
    # Repete a pergunta até receber uma opção que exista.
    exibir_menu_detalhado()

    print("\nSELEÇÃO DE PERSONAGEM")
    print("1. Cavaleiro")
    print("2. Paladino")
    print("3. Mago")
#laço de repetição para seleção
    while True:
        opcao = input("\nEscolha o seu personagem: \n")
        nome = input("Digite o nome do seu personagem: \n")

        if opcao == "1":
            return Cavaleiro(nome)

        elif opcao == "2":
            return Paladino(nome)

        elif opcao == "3":
            return Mago(nome)
        else:
            print("Opção incorreta! Escolha 1,2 ou 3.")

def torre(personagem):
    goblin = Goblin()
    orc = Orc()
    tyranid = Tyranid()
    nurgle = Nurgle()
    lista = [goblin, orc, tyranid, nurgle]

    print("Entrando na torre de combate!")

    for i in lista:
        print(f"O inimigo a ser encarado é: {i.nome}")
        print(i.descricao)
        print("\nStatus do inimigo:")
        print(f"Ataque: {i.stats.getAtaque()}")
        print(f"Defesa: {i.stats.getDefesa()}")
        print(f"Vida: {i.stats.getVida()}")

        combate = BatalhaManager(personagem, i)
        vencedor = combate.executar_turno()
        if vencedor is i:
            print(f"Game Over")
            break
        personagem.experiencia_ganha(i.dificuldade)

        print("\nStatus das Habilidades")
        print(f"Ataque: {personagem.stats.getAtaque()}")
        print(f"Defesa: {personagem.stats.getDefesa()}")
        print(f"Vida: {personagem.stats.getVida()}")

        personagem.distribuicao()



def main():
    # Começa escolhendo um herói e distribuindo os pontos de experiência.
    while True:
        jogador = escolher_personagem()
        print(f"\n{jogador.nome}, você escolheu seu personagem!")
        torre(jogador)

        print("Deseja jogar novamente? ")
        print("1 - Sim")
        print("2 - Não")
        continuar = True
        while continuar:
            escolha = input()
            if escolha == "2":
                print("Obrigado por jogar!")
                sys.exit()
            elif escolha == "1":
                print("Vamos jogar novamente!")
                continuar = False
            else:
                print("Comando inválido, escolha entre 1 e 2.")

    print("\nStatus das Habilidades")
    print(f"Ataque: {jogador.stats.getAtaque()}")
    print(f"Defesa: {jogador.stats.getDefesa()}")
    print(f"Vida: {jogador.stats.getVida()}")


if __name__ == "__main__":
    main()

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