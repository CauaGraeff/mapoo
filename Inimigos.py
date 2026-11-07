from Stats import Stats
import random

class Inimigos:

    def __init__(self, nome, dificuldade, ataque, defesa, vida):
        self.stats = Stats(ataque, defesa, vida)
        self.nome = nome
        self.dificuldade = dificuldade
        self.paralisado = False
        self.vida_perdida = 0
        self.prioridade = 0
        self.azarado = False
        self.sortudo = False
        self.carregamento_habilidade = 0

    def escolher_acao(self):
        pass

    def acoes(self, escolha: str, personagem):
        pass

    def usar_habilidade_ativa(self, personagem):
        pass

# INIMIGO FRACO - NIVEL 1
class Goblin(Inimigos):

    def __init__(self):
        super().__init__("Goblin", 1, 5, 20, 30)

    def escolher_acao(self):
        return "1"

    def acoes(self, escolha: str, personagem):
        dano = 3
        defesa = 0
        recuperacao_vida = 0
        diminuicao_ataque_inimigo = 0
        diminuicao_defesa_inimigo = 0

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


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
        diminuicao_defesa_inimigo = 0
        if escolha == "1":
            dano = 6

        elif escolha == "2":
            recuperacao_vida = 6

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


# INIMIGO FORTE - NIVEL 2
class Tyranid(Inimigos):

    def __init__(self):
        super().__init__("Tyranid", 3, 14, 8, 23)

        self.duracao_instinto_colmeia = 0
        self.instinto_colmeia = False

    def escolher_acao(self):
        if self.duracao_instinto_colmeia == 0:
            self.instinto_colmeia = False
        if not self.instinto_colmeia:
            return random.choice(["1", "2"])
        else:
            return "1"

    def acoes(self, escolha: str, personagem):
        dano = 0
        defesa = 0
        recuperacao_vida = 0
        diminuicao_ataque_inimigo = 0
        diminuicao_defesa_inimigo = 0

        if escolha == "1":
            dano = 17

        elif escolha == "2":
            self.instinto_colmeia = True
            self.duracao_instinto_colmeia = 2

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


# CHEFAO - NIVEL 3
class Nurgle(Inimigos):

    def __init__(self):
        super().__init__("Nurgle", 3, 18, 13, 30)

        self.modo_escudo_corrosivo = False
        self.apodrecimento = False
    def escolher_acao(self):
        if not self.modo_escudo_corrosivo:
            escolha = random.choice(["1", "2"])
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
        diminuicao_defesa_inimigo = 0

        if escolha == "1":
            self.prioridade = -5
            if (self.modo_escudo_corrosivo):
                self.modo_escudo_corrosivo = False
            elif (not self.modo_escudo_corrosivo):
                self.modo_escudo_corrosivo = True
                return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


        elif escolha == "2":
            dano = 18

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo

    def usar_habilidade_ativa(self, personagem):
        if self.carregamento_habilidade == 0:
            self.apodrecimento = True
            self.carregamento_habilidade = 4
        else:
            self.carregamento_habilidade -= 1


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