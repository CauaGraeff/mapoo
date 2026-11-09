"""Exemplo pequeno que começa uma luta entre um Paladino e um Goblin."""

# Importa as peças que serão usadas neste teste.
from Cavaleiro import Cavaleiro
from Inimigos import Inimigos, Goblin, Orc
from BatalhaManager import BatalhaManager
from Mago import Mago
from Paladino import Paladino

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


# Cria os dois lutadores.
personagem = escolher_personagem()
goblin = Goblin()
orc = Orc()

# Prepara a batalha com o herói e o monstro.
teste = BatalhaManager(personagem, goblin)
# Começa os turnos até que alguém vença.
#teste.executar_turno()
personagem.experiencia_ganha(goblin.dificuldade)
personagem.distribuicao()

teste2 = BatalhaManager(personagem, orc)
teste2.executar_turno()
personagem.experiencia_ganha(orc.dificuldade)

personagem.distribuicao()

print("Fim do teste")