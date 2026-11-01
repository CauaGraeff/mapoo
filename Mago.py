from Personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, ataque = 10, defesa = 5, vida = 7)
        self.modo_carregamento = False
    def escolher_acao(self):
        while(True):
            if(not self.modo_carregamento):
                escolha = input("Escolha uma ação do paladino: \n"
                      "1 - Bola de fogo \n"
                      "2 - Super bola de fogo \n")
            else:
                escolha = "2"

            if(escolha != "1" and escolha != "2"):
                print("Opção invalida!")
                continue
            return escolha
    def acoes(self, escolha: str, inimigo):
        if (escolha == "1"):
            dano = 5
            defesa = 0
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 0
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo
        elif (escolha == "2"):
            dano = 13
            defesa = 0
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 0
            if (self.modo_carregamento):
                self.modo_carregamento = False
                return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo
            elif (not self.modo_carregamento):
                self.modo_carregamento = True
                return 0, 0, 0, 0
    def usar_habilidade_ativa(self):
        while (True):
            if(self.modo_carregamento == 0):

                escolha = input("Desejar usar uma de suas habilidades? "
                                "1 - sim"
                                "2 - não")
                if(escolha == "1"):
                    habilidade = input("Qual habidade? "
                                    "1 - Raio paralisante"
                                    "2 - Double luck"
                                    "3 - Escudo imperfeito")
                    if(habilidade == "1"):
                        break
                    elif(habilidade == "2"):
                        break
                    elif(habilidade == "3"):
                        break
                    else:
                        print("Opção invalida!")
                elif(escolha == "2"):
                    break
                else:
                    print("Opção invalida!")
            else:
                print(f"A habilidade está carregando, faltam {self.carregamento_habilidade} para poder utilizar novamente")
                self.carregamento_habilidade -= 1
                break