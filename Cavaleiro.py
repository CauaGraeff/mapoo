from Personagem import Personagem

class Cavaleiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 6, 10, 12)
    modo_defensivo = False

    def acao(self):
        while(True):
            if(not self.modo_defensivo):
                escolha = input("Escolha uma ação do cavaleiro: "
                    "1 - Corte Rápido"
                    "2 - Defesa sólida")
            else:
                escolha = "2"
            if (escolha == "1"):
                dano = 5
                defesa = 0
                recuperacao_vida = 0
                return dano, defesa, recuperacao_vida
            elif (escolha == "2"):
                dano = 0
                defesa = 5
                recuperacao_vida = 0
                if(self.modo_defensivo):
                    self.modo_defensivo = False
                elif(not self.modo_defensivo):
                    self.modo_defensivo = True
                return dano, defesa, recuperacao_vida
            else:
                print("Opção invalida!")
                continue
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
