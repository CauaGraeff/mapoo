from Personagem import Personagem

class Paladino(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 7, 8, 8)

    def acao(self):
        escolha = input("Escolha uma ação do paladino: "
              "1 - Recuperação de vida"
              "2 - Corte prejudicial")
        if(escolha == "1"):
           pass
        elif(escolha == "2"):
            pass
        else:
            print("Opção invalida!")
    def usar_habilidade_ativa(self):
        escolha = input("Desejar usar a sua habilidade 'Vida emergencial'? "
                        "1 - sim"
                        "2 - não")
        if(escolha == "1"):
            pass
        elif(escolha == "2"):
            pass
        else:
            print("Opção invalida!")