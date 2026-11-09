"""Cria os monstros e descreve as ações de cada um."""

from Stats import Stats
import random

class Inimigos:

    def __init__(self, nome, dificuldade, ataque, defesa, vida):
        # Todos os monstros começam com estas informações em comum.
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
        # Cada tipo de monstro escolhe sua ação de um jeito próprio.
        pass

    def acoes(self, escolha: str, personagem):
        # Cada monstro informa dano, defesa, cura e enfraquecimentos.
        pass

    def usar_habilidade_ativa(self, personagem):
        # Monstros sem poder especial não fazem nada aqui.
        pass

# INIMIGO FRACO - NIVEL 1
class Goblin(Inimigos):

    def __init__(self):
        super().__init__("Goblin", 1, 5, 10, 30)

    def escolher_acao(self):
        return "1"

    def acoes(self, escolha: str, personagem):
        # O Goblin sempre tenta causar um pouco de dano.
        # Os outros valores ficam zerados porque ele não cura nem se defende.
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
        # O Orc escolhe ao acaso entre atacar e se curar.
        return random.choice(["1", "2"])

    def acoes(self, escolha: str, personagem):
        dano = 0
        defesa = 0
        recuperacao_vida = 0
        diminuicao_ataque_inimigo = 0
        diminuicao_defesa_inimigo = 0
        if escolha == "1":
            # Ataque do Orc: causa dano ao herói.
            dano = 6

        elif escolha == "2":
            # Cura do Orc: recupera vida em vez de atacar.
            recuperacao_vida = 6

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


# INIMIGO FORTE - NIVEL 2
class Tyranid(Inimigos):

    def __init__(self):
        super().__init__("Tyranid", 3, 14, 8, 23)

        self.duracao_instinto_colmeia = 0
        self.instinto_colmeia = False

    def escolher_acao(self):
        # Quando ativa o instinto, o Tyranid prefere atacar.
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
            # O ataque do Tyranid causa bastante dano.
            dano = 17

        elif escolha == "2":
            # O instinto dura dois turnos e melhora as rolagens de ataque.
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
        # Com o escudo desligado, Nurgle escolhe entre se proteger ou atacar.
        if not self.modo_escudo_corrosivo:
            escolha = random.choice(["1", "2"])
            return escolha
        else:
            # Enquanto o escudo está ligado, Nurgle escolhe a ação de proteção.
            return "1"

    def acoes(self, escolha: str, personagem):
        dano = 0
        defesa = 0
        recuperacao_vida = 0
        diminuicao_ataque_inimigo = 0
        diminuicao_defesa_inimigo = 0

        if escolha == "1":
            # Liga ou desliga o escudo corrosivo; ao ligá-lo, não causa dano.
            if (self.modo_escudo_corrosivo):
                self.modo_escudo_corrosivo = False
                self.prioridade = 0
            elif (not self.modo_escudo_corrosivo):
                self.modo_escudo_corrosivo = True
                self.prioridade = 5
                return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


        elif escolha == "2":
            # O ataque forte de Nurgle causa dano ao herói.
            dano = 18

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo

    def usar_habilidade_ativa(self, personagem):
        # A habilidade de Nurgle enfraquece o herói por alguns turnos.
        if self.carregamento_habilidade == 0:
            # Ativa o apodrecimento e começa a recarga de quatro turnos.
            self.apodrecimento = True
            self.carregamento_habilidade = 4
        else:
            # A contagem diminui até a habilidade poder ser usada outra vez.
            self.carregamento_habilidade -= 1


# TESTES
if __name__ == "__main__":

    # Estas linhas mostram como criar cada monstro e ver uma ação sua.
    goblin = Goblin()
    orc = Orc()
    tyranid = Tyranid()
    nurgle = Nurgle()

    print(goblin.nome, goblin.escolher_acao())
    print(orc.nome, orc.escolher_acao())
    print(tyranid.nome, tyranid.escolher_acao())
    print(nurgle.nome, nurgle.escolher_acao())