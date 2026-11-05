from Paladino import Paladino
from Cavaleiro import Cavaleiro
from Inimigos import Goblin, Orc, Tyranid, Nurgle
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
        opcao = input("\nEscolha o seu personagem: ").strip()

        if opcao != "1" and opcao != "2" and opcao != "3":
            print("Opção incorreta! Escolha 1,2 ou 3.")
            continue

        break

#laço de repetição para o nome do personagem
    while True:
        nome = input("Digite o nome do seu personagem: ").strip()

        if nome == "":
            print("O nome do personagem não pode ficar vazio.")
            continue

        break

    if opcao == "1":
        return Cavaleiro(nome)

    elif opcao == "2":
        return Paladino(nome)

    else:
        return Mago(nome)

#função para calcular o dano de um ataque
def calcular_ataque(atacante, defensor, dano_acao):
    # 1. Rola o dado de 1 a 20
    dado = random.randint(1, 20)

    # 2. Se o atacante estiver azarado, rola dois dados e usa o menor
    if (getattr(atacante, "azarado", False)):
        dado = min(dado, random.randint(1, 20))

    # 3. Calcula o dano bruto (Dado + Ataque + Dano da ação)
    dano_bruto = dado + atacante.stats.getAtaque() + dano_acao

    # 4. Subtrai a defesa do defensor (inclusive a defesa temporária)
    dano_final = dano_bruto - defensor.stats.getDefesa() - getattr(defensor, "defesa_temporaria", 0)

    # 5. Garante o dano mínimo de 1 (para o ataque nunca ser inútil)
    if dano_final < 1:
        dano_final = 1

    return dano_final

#função para aplicar o resultado de uma ação
def aplicar_acao(atacante, defensor, dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo):
    atacante.defesa_temporaria = defesa

    if (dano > 0):
        dano_final = calcular_ataque(atacante, defensor, dano)
        defensor.stats.setVida(-dano_final)
        defensor.vida_perdida = defensor.vida_maxima - defensor.stats.getVida()
        print(f"{atacante.nome} causou {dano_final} de dano em {defensor.nome}!")

    if (recuperacao_vida > 0):
        defensor.stats.setVida(int(recuperacao_vida))
        if (defensor.stats.getVida() > defensor.vida_maxima):
            defensor.stats.setVida(defensor.vida_maxima - defensor.stats.getVida())
        defensor.vida_perdida = defensor.vida_maxima - defensor.stats.getVida()
        print(f"{defensor.nome} recuperou {int(recuperacao_vida)} de vida!")

    if (diminuicao_ataque_inimigo > 0):
        defensor.stats.setAtaque(-diminuicao_ataque_inimigo)
        print(f"{defensor.nome} perdeu {diminuicao_ataque_inimigo} de ataque!")

#função para um combate
def combate(jogador, inimigo):
    print(f"\n{jogador.nome} x {inimigo.nome}")

    jogador.usar_habilidade_ativa(inimigo)

    while (jogador.stats.getVida() > 0 and inimigo.stats.getVida() > 0):
        print(f"\nVida de {jogador.nome}: {jogador.stats.getVida()} | Vida de {inimigo.nome}: {inimigo.stats.getVida()}")

        # A defesa temporária vale apenas para este turno
        jogador.defesa_temporaria = 0
        inimigo.defesa_temporaria = 0

        escolha = jogador.escolher_acao()
        dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo = jogador.acoes(escolha, inimigo)
        aplicar_acao(jogador, inimigo, dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo)

        if (inimigo.stats.getVida() <= 0):
            break

        if (inimigo.paralisado):
            print(f"{inimigo.nome} está paralisado e não pode atacar!")
            inimigo.paralisado = False
            continue

        escolha = inimigo.escolher_acao()
        dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo = inimigo.acoes(escolha, jogador)
        aplicar_acao(inimigo, jogador, dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo)

    if (jogador.stats.getVida() <= 0):
        print(f"\n{jogador.nome} foi derrotado por {inimigo.nome}...")
        return False

    print(f"\n{jogador.nome} venceu o {inimigo.nome}!")
    return True

def main():
    jogador = escolher_personagem()
    print(f"\n{jogador.nome} seu personagem foi selecionado!")

    jogador.experiencia_ganha(3)
    jogador.distruicao()

    print("\nStatus das Habilidades")
    print(f"Ataque: {jogador.stats.getAtaque()}")
    print(f"Defesa: {jogador.stats.getDefesa()}")
    print(f"Vida: {jogador.stats.getVida()}")

    inimigos = [Goblin(), Orc(), Tyranid(), Nurgle()]
    venceu = True

    for inimigo in inimigos:
        if (not combate(jogador, inimigo)):
            venceu = False
            break

        # Recupera toda a vida após derrotar o inimigo
        jogador.stats.setVida(jogador.vida_maxima - jogador.stats.getVida())
        jogador.vida_perdida = 0
        print(f"{jogador.nome} recuperou toda a vida!")

        jogador.experiencia_ganha(inimigo.dificuldade)
        jogador.distruicao()

    if (venceu):
        print(f"\nParabéns {jogador.nome}! Você venceu todos os inimigos!")

if __name__ == "__main__":
    main()