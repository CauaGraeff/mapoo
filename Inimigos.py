import random

from Personagem import Personagem


class Inimigos(Personagem):
    """
    Classe base de todos os inimigos.

    Herda de Personagem para reaproveitar Stats, experiencia, prioridade e
    vida_perdida. Mantem o mesmo contrato das classes jogaveis (Cavaleiro,
    Mago e Paladino):

        escolha = inimigo.escolher_acao()
        dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo = \
            inimigo.acoes(escolha, jogador)

    A diferenca e que o inimigo escolhe a acao sozinho, sem input.
    """

    def __init__(self, nome, ataque, defesa, vida, dificuldade=1, prioridade=0):
        super().__init__(nome, ataque, defesa, vida)
        self.dificuldade = dificuldade
        self.prioridade = prioridade
        self.vida_maxima = vida
        self.azarado = False
        self.paralisado = False

    # ------------------------------------------------------------------
    # Estado e vida
    # ------------------------------------------------------------------
    @property
    def vivo(self):
        return self.stats.getVida() > 0

    def status(self):
        return (f"{self.nome} | vida: {self.stats.getVida()}/{self.vida_maxima} "
                f"| ataque: {self.stats.getAtaque()} "
                f"| defesa: {self.stats.getDefesa()} "
                f"| dificuldade: {self.dificuldade}")

    def receber_dano(self, dano):
        """Aplica o dano usando Stats e devolve o dano realmente recebido."""
        dano = max(0, int(dano))
        if dano == 0 or not self.vivo:
            return 0

        vida_antes = self.stats.getVida()
        self.stats.setVida(-dano)

        # Stats trabalha com soma, entao a vida nunca deve ficar negativa.
        if self.stats.getVida() < 0:
            self.stats.setVida(-self.stats.getVida())

        dano_aplicado = vida_antes - self.stats.getVida()
        self.vida_perdida += dano_aplicado
        return dano_aplicado

    def curar(self, quantidade):
        """Recupera vida sem ultrapassar a vida maxima do inimigo."""
        quantidade = max(0, int(quantidade))
        if quantidade == 0 or not self.vivo:
            return 0

        espaco_livre = self.vida_maxima - self.stats.getVida()
        cura = min(quantidade, max(0, espaco_livre))
        if cura:
            self.stats.setVida(cura)
            self.vida_perdida = max(0, self.vida_perdida - cura)
        return cura

    # ------------------------------------------------------------------
    # Acoes
    # ------------------------------------------------------------------
    def acoes_disponiveis(self):
        """Deve retornar as escolhas possiveis do inimigo."""
        raise NotImplementedError

    def escolher_acao(self, inimigo=None):
        """Escolhe uma acao automaticamente, sem pedir input ao jogador."""
        if not self.vivo:
            return "0"

        if self.paralisado:
            return "0"

        return random.choice(self.acoes_disponiveis())

    def acoes(self, escolha: str, inimigo):
        """
        Executa a acao escolhida.

        Retorna a mesma tupla usada pelas classes jogaveis:
        (dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo).
        """
        if escolha == "0":
            if self.paralisado:
                self.paralisado = False
            return 0, 0, 0, 0

        # Integra com a habilidade "O azarao" do Cavaleiro.
        # O efeito dura um turno e da 50% de chance de o ataque errar.
        if self.azarado:
            self.azarado = False
            if random.random() < 0.5:
                return 0, 0, 0, 0

        return self.executar_acao(escolha, inimigo)

    def executar_acao(self, escolha: str, inimigo):
        """Implementado por cada inimigo concreto."""
        raise NotImplementedError


class Goblim(Inimigos):
    """Inimigo fraco e rapido, comum no inicio do jogo."""

    def __init__(self, nome="Goblim"):
        super().__init__(nome, ataque=4, defesa=2, vida=6,
                         dificuldade=1, prioridade=1)

    def acoes_disponiveis(self):
        return ["1", "2", "3"]

    def executar_acao(self, escolha: str, inimigo):
        if escolha == "1":
            # Mordida
            return 3, 0, 0, 0
        elif escolha == "2":
            # Punhalada
            return 4, 0, 0, 0
        elif escolha == "3":
            # Defesa improvisada
            return 0, 2, 0, 0
        return 0, 0, 0, 0


class Orc(Inimigos):
    """Inimigo resistente e forte, com um buff unico de ataque."""

    def __init__(self, nome="Orc"):
        super().__init__(nome, ataque=7, defesa=5, vida=12,
                         dificuldade=2, prioridade=0)
        self.grito_usado = False

    def acoes_disponiveis(self):
        if self.grito_usado:
            return ["1", "3"]
        return ["1", "2", "3"]

    def executar_acao(self, escolha: str, inimigo):
        if escolha == "1":
            # Golpe de machado
            return 6, 0, 0, 0
        elif escolha == "2":
            # Grito de guerra: aumenta o proprio ataque uma unica vez
            if not self.grito_usado:
                self.grito_usado = True
                self.stats.setAtaque(2)
            return 0, 0, 0, 0
        elif escolha == "3":
            # Postura defensiva
            return 0, 4, 0, 0
        return 0, 0, 0, 0


class DemonioChefe(Inimigos):
    """Chefe final: fica mais perigoso quando esta com metade da vida."""

    def __init__(self, nome="Demonio Chefe"):
        super().__init__(nome, ataque=9, defesa=7, vida=25,
                         dificuldade=3, prioridade=2)
        self.fase = 1

    def receber_dano(self, dano):
        dano_aplicado = super().receber_dano(dano)
        self.atualizar_fase()
        return dano_aplicado

    def atualizar_fase(self):
        if self.fase == 1 and self.vivo and self.stats.getVida() <= self.vida_maxima // 2:
            self.fase = 2
        return self.fase

    def acoes_disponiveis(self):
        self.atualizar_fase()
        if self.fase == 2:
            return ["1", "2", "3", "4", "5"]
        return ["1", "2", "3", "4"]

    def executar_acao(self, escolha: str, inimigo):
        self.atualizar_fase()

        if escolha == "1":
            # Garra infernal (mais forte na segunda fase)
            dano = 9 if self.fase == 2 else 7
            return dano, 0, 0, 0
        elif escolha == "2":
            # Bola de fogo infernal
            return 10, 0, 0, 0
        elif escolha == "3":
            # Drenar vida: causa dano e recupera parte da propria vida
            return 5, 0, 5, 0
        elif escolha == "4":
            # Maldicao: reduz o ataque do inimigo (jogador)
            return 0, 0, 0, 4
        elif escolha == "5" and self.fase == 2:
            # Furia infernal: ataque devastador exclusivo da segunda fase
            return 12, 0, 0, 0
        return 0, 0, 0, 0


def criar_inimigo(tipo, nome=None):
    """
    Fabrica de inimigos.

    Aceita: "goblim"/"goblin", "orc" e "demonio"/"demonio chefe".
    """
    tipo = tipo.strip().lower()

    classes = {
        "goblim": Goblim,
        "goblin": Goblim,
        "orc": Orc,
        "demonio": DemonioChefe,
        "demonio chefe": DemonioChefe,
        "chefe": DemonioChefe,
    }

    if tipo not in classes:
        raise ValueError(f"Tipo de inimigo invalido: {tipo}")

    if nome is None:
        return classes[tipo]()
    return classes[tipo](nome)


if __name__ == "__main__":
    for inimigo in (Goblim(), Orc(), DemonioChefe()):
        escolha = inimigo.escolher_acao()
        acao = inimigo.acoes(escolha, None)
        print(f"{inimigo.status()} | acao: {escolha} -> {acao}")
