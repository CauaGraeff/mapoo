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
        super().__init__("Goblin", 1, 3, 2, 8)
        self.descricao = "O Goblin combina um golpe desajeitado com uma defesa fraca para derrotar quem invade a torre"

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
        print("Goblin está utilizando a ação golpe desajeitado!")

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


# INIMIGO MEDIO - NIVEL 1
class Orc(Inimigos):

    def __init__(self):
        super().__init__("Orc", 2, 6, 6, 15)
        self.descricao = "O Orc é uma criatura com muita vida, que se você não se cuidar para o inicio voltará"

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
            print("Orc está utilizando a ação machadada devastadora!")

        elif escolha == "2":
            # Cura do Orc: recupera vida em vez de atacar.
            recuperacao_vida = 6
            print("Orc está utilizando a ação WAAG!")

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


# INIMIGO FORTE - NIVEL 2
class Tyranid(Inimigos):

    def __init__(self):
        super().__init__("Tyranid", 3, 14, 8, 23)
        self.descricao = "Tyranid possui alto ataque combinado com maior status de vida, utiliza ligação psíquica para ganhar vantagem no turno"
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
            dano = 8
            print("Tyranid está utilizando a ação garra corrosiva!")

        elif escolha == "2":
            # O instinto dura dois turnos e melhora as rolagens de ataque.
            self.instinto_colmeia = True
            self.duracao_instinto_colmeia = 2
            print("Tyranid está utilizando a ação instinto colmeia!"
                  "Agora ele gira dois dados e pega o melhor resultado!")

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


# CHEFAO - NIVEL 3
class Nurgle(Inimigos):

    def __init__(self):
        super().__init__("Nurgle", 3, 18, 13, 30)
        self.descricao = "Enfim chegamos ao chefão, com a maior vida entre os inimigos, para vencê-lo é necessário encarar o seu escudo corrosivo combinado com seu ataque que desnorteia o jogador."
        self.modo_escudo_corrosivo = False
        self.apodrecimento = False
        self.duracao_escudo_corrosivo = 0
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
                self.duracao_escudo_corrosivo = 0
                self.prioridade = 0
                print("Nurgle está utilizando a ação escudo corrosivo!")
            elif (not self.modo_escudo_corrosivo):
                self.modo_escudo_corrosivo = True
                self.prioridade = 5
                self.duracao_escudo_corrosivo = 1
                print("Nurgle está utilizando a ação escudo corrosivo!")
                return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo


        elif escolha == "2":
            # O ataque forte de Nurgle causa dano ao herói.
            print("Nurgle está utilizando a ação praga corrosiva!")
            dano = 10

        return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo

    def usar_habilidade_ativa(self, personagem):
        # A habilidade de Nurgle enfraquece o herói por alguns turnos.
        if self.carregamento_habilidade == 0:
            # Ativa o apodrecimento e começa a recarga de quatro turnos.
            self.apodrecimento = True
            self.carregamento_habilidade = 4
            print("Nurgle está utilizando a habilidade apodrecimento!")
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