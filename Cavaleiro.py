from Personagem import Personagem

class Cavaleiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 6, 10, 12)

    def acao(self):
        escolha = input("Escolha uma ação do cavaleiro: "
              "1 - Corte Rápido"
              "2 - Defesa sólida")
        if(escolha == "1"):
            pass
        elif(escolha == "2"):
            pass
        else:
            print("Opção invalida!")
    def usar_habilidade_ativa(self):
        escolha = input("Desejar usar a sua habilidade 'O azarão'? "
                        "1 - sim"
                        "2 - não")
        if(escolha == "1"):
            pass
        elif(escolha == "2"):
            pass
        else:
            print("Opção invalida!")
