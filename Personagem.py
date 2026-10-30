from Stats import Stats

class Personagem:

    def __init__(self, nome, ataque, defesa, vida):
        self.nome = nome
        self.stats = Stats(ataque, defesa, vida)
        self.experiencia = 0

    def acao(self):
        pass

    def experiencia_ganha(self, dificuldade):
        if(dificuldade == 1):
            self.experiencia += 2
        elif (dificuldade == 2):
            self.experiencia += 4
        elif (dificuldade == 3):
            self.experiencia += 5

    def distruicao(self):
        while(True):
            print(f"Tu tem no momento essa quantidade de experiência {self.experiencia},"
                  f"coloque como tu deseja distribuir os pontos de experiência do personagem na seguinte forma:"
                  f"ataque, defesa, vida")
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
                break