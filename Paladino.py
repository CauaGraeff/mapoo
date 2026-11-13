"""Define as ações de cura e o poder especial do Paladino."""

from Personagem import Personagem

class Paladino(Personagem):
    def __init__(self, nome):
        # O Paladino mistura ataque, defesa e recuperação de vida.
        super().__init__(nome, ataque = 7, defesa = 8, vida = 8)
        self.vida_emergencial = False
        self.vida_extra = 0
        self.recuperacao_vida = False

    def escolher_acao(self):
        # A ação de recuperação faz o Paladino agir depois do inimigo.
        while(True):
            self.prioridade = 0
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
            # Prepara a recuperação: primeiro o Paladino recebe o golpe.
            dano = 0
            defesa = 0
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 0
            diminuicao_defesa_inimigo = 0
            self.recuperacao_vida = True
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo
        elif(escolha == "2"):
            # Corte Prejudicial ataca e reduz o ataque do inimigo neste turno.
            dano = 7
            defesa = 0
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 5
            diminuicao_defesa_inimigo = 0
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo
    def usar_habilidade_ativa(self, inimigo):
        # Vida Emergencial dá ao Paladino uma reserva temporária de 5 pontos de vida.
        while (True):
            if self.carregamento_habilidade == 3:
                # Ao chegar a esta parte da recarga, o efeito temporário termina.
                self.vida_emergencial = False
            if (self.carregamento_habilidade == 0):
                escolha = input("Desejar usar a sua habilidade 'Vida emergencial'? \n"
                                "1 - sim \n"
                                "2 - não \n")
                if(escolha == "1"):
                    # Ativa a vida extra e começa a recarga do poder.
                    self.vida_emergencial = True
                    self.carregamento_habilidade = 5
                    self.vida_extra = 5
                    break
                elif(escolha == "2"):
                    break
                else:
                    print("Opção invalida!")
            else:
                # Avança a recarga depois que a habilidade foi usada.
                if self.carregamento_habilidade <= 3:
                    print(f"A habilidade está carregando, faltam {self.carregamento_habilidade} para poder utilizar novamente")
                self.carregamento_habilidade -= 1
                break