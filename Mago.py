from Personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 10, 5, 7)

    def acao(self):
        escolha = input("Escolha uma ação do paladino: "
              "1 - Bola de fogo"
              "2 - Super bola de fogo")
        if(escolha == "1"):
            dano = 5
            return dano
        elif(escolha == "2"):
            dano = 13
        else:
            print("Opção invalida!")
    def usar_habilidade_ativa(self):
        escolha = input("Desejar usar uma de suas habilidades? "
                        "1 - sim"
                        "2 - não")
        if(escolha == "1"):
            habilidade = input("Qual habidade? "
                            "1 - Raio paralisante"
                            "2 - Double luck"
                            "3 - Escudo imperfeito")
            if(habilidade == "1"):
                pass
            elif(habilidade == "2"):
                pass
            elif(habilidade == "3"):
                pass
            else:
                print("Opção invalida!")
        elif(escolha == "2"):
            pass
        else:
            print("Opção invalida!")