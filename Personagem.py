from Stats import Stats

class Personagem:

    def __init__(self, nome, ataque, defesa, vida):
        self.nome = nome
        self.stats = Stats(ataque, defesa, vida)
        self.experiencia = 0
        self.vida_perdida = 0
        self.prioridade = 0
        self.carregamento_habilidade = 0

    def escolher_acao(self):
        pass
    def acoes(self):
        pass

    def experiencia_ganha(self, dificuldade):
        if(dificuldade == 1):
            self.experiencia += 2
        elif (dificuldade == 2):
            self.experiencia += 4
        elif (dificuldade == 3):
            self.experiencia += 5
        else:
            print("Entrada invalida.")

    def distruicao(self):
        while(True):
            try:
                print(f"Tu tem no momento essa quantidade de experiência {self.experiencia}, \n"
                      f"coloque como tu deseja distribuir os pontos de experiência do personagem na seguinte forma: \n"
                      f"ataque, defesa, vida \n")
                x, y, z = map(int, input().split())
                if(x < 0 or y < 0 or z < 0):
                    print("Você não pode digitar valor negativo.")
                    continue
                elif(x + y + z > self.experiencia):
                    print("Você não pode fazer a soma de distribuição ser maior que experiência")
                    continue
                else:
                    self.stats.setAtaque(x)
                    self.stats.setDefesa(y)
                    self.stats.setVida(z)
                    self.experiencia -= (x + y + z)
                    break
            except ValueError:
                print("Você não pode digitar caracteres diferentes de números ou deixar um valor da variável vazia.")