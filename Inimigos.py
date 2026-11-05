from Stats import Stats
import random

class Inimigos:

    def __init__(self, nome, dificuldade, ataque, defesa, vida):
        self.stats = Stats(ataque, defesa, vida)
        self.nome = nome
        self.dificuldade = dificuldade
        self.paralisado = False
        self.vida_perdida = 0
        self.vida_maxima = vida
        self.prioridade = 0
        self.defesa_temporaria = 0
        self.azarado = False

    def escolher_acao(self):
        pass

    def acoes(self, escolha: str, personagem):
        pass


# INIMIGO FRACO - NIVEL 1
class Goblin(Inimigos):

    def __init__(self):
        super().__init__("Goblin", 1, 3, 2, 8)

    def escolher_acao(self):
        return "1"

    def acoes(self, escolha: str, personagem):
        dano = 3
        defesa = 0
        recuperacao_vida = 0
        diminuicao_ataque_inimigo = 0

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo


# INIMIGO MEDIO - NIVEL 1
class Orc(Inimigos):

    def __init__(self):
        super().__init__("Orc", 2, 6, 6, 15)

    def escolher_acao(self):
        return random.choice(["1", "2"])

    def acoes(self, escolha: str, personagem):
        dano = 0
        defesa = 0
        recuperacao_vida = 0
        diminuicao_ataque_inimigo = 0

        if escolha == "1":
            dano = 6

        elif escolha == "2":
            recuperacao_vida = 6

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo


# INIMIGO FORTE - NIVEL 2
class Tyranid(Inimigos):

    def __init__(self):
        super().__init__("Tyranid", 3, 14, 8, 23)

        self.instinto_colmeia = False

    def escolher_acao(self):
        return random.choice(["1", "2"])

    def acoes(self, escolha: str, personagem):
        dano = 0
        defesa = 0
        recuperacao_vida = 0
        diminuicao_ataque_inimigo = 0

        if escolha == "1":
            dano = 17

        elif escolha == "2":
            self.instinto_colmeia = True

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo


# CHEFAO - NIVEL 3
class Nurgle(Inimigos):

    def __init__(self):
        super().__init__("Nurgle", 3, 18, 13, 30)

        self.modo_escudo_corrosivo = False
        self.apodrecimento = 0
        self.bomba_veneno = 0

    def escolher_acao(self):
        if not self.modo_escudo_corrosivo:
            escolha = random.choice(["1", "2", "3", "4"])
            if escolha == "1":
                self.prioridade = -5
            return escolha
        else:
            return "1"

    def acoes(self, escolha: str, personagem):
        dano = 0
        defesa = 0
        recuperacao_vida = 0
        diminuicao_ataque_inimigo = 0

        if escolha == "1":
            dano = 10
            if (self.modo_escudo_corrosivo):
                self.modo_escudo_corrosivo = False
            else:
                self.modo_escudo_corrosivo = True
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo

        elif escolha == "2":
            dano = 18

        elif escolha == "3":
            self.apodrecimento = 2
            diminuicao_ataque_inimigo = 7

        elif escolha == "4":
            self.bomba_veneno = 3

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo


# TESTES
if __name__ == "__main__":

    goblin = Goblin()
    orc = Orc()
    tyranid = Tyranid()
    nurgle = Nurgle()

    print(goblin.nome, goblin.escolher_acao())
    print(orc.nome, orc.escolher_acao())
    print(tyranid.nome, tyranid.escolher_acao())
    print(nurgle.nome, nurgle.escolher_acao())