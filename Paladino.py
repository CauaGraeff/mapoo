from Personagem import Personagem

class Paladino(Personagem):
    def __init__(self, nome):
        super().__init__(nome, ataque = 7, defesa = 8, vida = 8)

    def escolher_acao(self):
        while(True):
            escolha = input("Escolha uma ação do paladino: \n"
                  "1 - Recuperação de vida \n"
                  "2 - Corte prejudicial \n")
            if(escolha == "1"):
                self.prioridade = -1
            if(escolha != "1" and escolha != "2"):
                print("Opção invalida!")
                continue
            return escolha
    def acoes(self, escolha: str, inimigo):
        if(escolha == "1"):
            dano = 0
            defesa = 0
            recuperacao_vida = self.vida_perdida * 0.5
            diminuicao_ataque_inimigo = 0
            self.prioridade = 0
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo
        elif(escolha == "2"):
            dano = 5
            defesa = 0
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 5
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo
    def usar_habilidade_ativa(self):
        while (True):
            if (self.carregamento_habilidade == 0):
                escolha = input("Desejar usar a sua habilidade 'Vida emergencial'? "
                                "1 - sim"
                                "2 - não")
                if(escolha == "1"):
                    break
                elif(escolha == "2"):
                    break
                else:
                    print("Opção invalida!")
            else:
                print(f"A habilidade está carregando, faltam {self.carregamento_habilidade} para poder utilizar novamente")
                self.carregamento_habilidade -= 1
                break