class Stats:
    __ataque = 0
    __vida = 0
    __defesa = 0
    def __init__(self, ataque, defesa, vida):
        self.__ataque = ataque
        self.__vida = vida
        self.__defesa = defesa

    def getVida(self):
        return self.__vida
    def getAtaque(self):
        return self.__ataque
    def getDefesa(self):
        return self.__defesa

    def setVida(self, vida):
        self.__vida += vida
    def setAtaque(self, ataque):
        self.__ataque += ataque
    def setDefesa(self, defesa):
        self.__defesa += defesa