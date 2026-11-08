"""Define as ações e o poder especial do Cavaleiro."""

from Personagem import Personagem

class Cavaleiro(Personagem):
    def __init__(self, nome):
        # O Cavaleiro começa com bastante defesa.
        super().__init__(nome, ataque = 6, defesa = 10, vida = 12)
        self.modo_defensivo = False

    def escolher_acao(self):
        # Pede uma opção até o jogador escolher uma ação válida.
        while(True):
            if(not self.modo_defensivo):
                escolha = input("Escolha uma ação do cavaleiro: \n"
                    "1 - Corte Rápido \n"
                    "2 - Defesa sólida \n")
            else:
                escolha = "2"
            if(escolha != "1" and escolha != "2"):
                print("Opção invalida!")
                continue
            return escolha
    def acoes(self, escolha: str, inimigo):
        if (escolha == "1"):
            # Corte Rápido causa dano e não aumenta a defesa.
            dano = 5
            defesa = 0
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 0
            diminuicao_defesa_inimigo = 0
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo
        elif (escolha == "2"):
            # Defesa Sólida reduz o dano recebido; a postura dura dois turnos.
            dano = 0
            defesa = 10
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 0
            diminuicao_defesa_inimigo = 0
            if (self.modo_defensivo):
                self.modo_defensivo = False
            elif (not self.modo_defensivo):
                self.modo_defensivo = True
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo

    def usar_habilidade_ativa(self, inimigo):
        # "O Azarão" faz o inimigo rolar dois dados e usar o menor.
        while(True):
            if (self.carregamento_habilidade == 0):
                escolha = input("Desejar usar a sua habilidade 'O azarão'? \n"
                                "1 - sim \n"
                                "2 - não \n")
                if(escolha == "1"):
                    # Marca o inimigo como azarado e inicia a recarga de 3 turnos.
                    inimigo.azarado = True
                    self.carregamento_habilidade = 3
                    break
                elif(escolha == "2"):
                    print("Habilidade não utilizada!")
                    break
                else:
                    print("Opção invalida!")
                    continue
            else:
                # Diminui a recarga um turno por vez.
                print(f"A habilidade está carregando, faltam {self.carregamento_habilidade} para poder utilizar novamente")
                self.carregamento_habilidade -= 1
                break