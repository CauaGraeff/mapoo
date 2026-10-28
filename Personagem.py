from Stats import Stats

class Personagem:

    def __init__(self, nome):
        self.nome = nome
        self.stats = Stats(5, 4, 8)
