"""Define as ações mágicas e os poderes do Mago."""

from Personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome):
        # O Mago ataca forte, mas tem pouca vida e defesa.
        super().__init__(nome, ataque = 10, defesa = 5, vida = 7)
        self.modo_carregamento = False
        self.escudo_imperfeito = False
    def escolher_acao(self):
        # Se a Super Bola de Fogo está carregando, ela será disparada automaticamente.
        while(True):
            if(not self.modo_carregamento):
                escolha = input("Escolha uma ação do paladino: \n"
                      "1 - Bola de fogo \n"
                      "2 - Super bola de fogo \n")
            else:
                escolha = "2"

            if(escolha != "1" and escolha != "2"):
                print("Opção invalida!")
                continue
            return escolha
    def acoes(self, escolha: str, inimigo):
        if (escolha == "1"):
            # Bola de Fogo é o ataque simples do Mago.
            dano = 5
            defesa = 0
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 0
            diminuicao_defesa_inimigo = 0
            return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo
        elif (escolha == "2"):
            # A Super Bola causa mais dano, mas primeiro precisa de um turno para carregar.
            dano = 13
            defesa = 0
            recuperacao_vida = 0
            diminuicao_ataque_inimigo = 0
            diminuicao_defesa_inimigo = 0
            if (self.modo_carregamento):
                # O disparo foi feito: termina o carregamento.
                self.modo_carregamento = False
                return dano, defesa, recuperacao_vida, diminuicao_ataque_inimigo, diminuicao_defesa_inimigo
            elif (not self.modo_carregamento):
                # Neste turno o Mago carrega o golpe, sem atacar.
                self.modo_carregamento = True
                return 0, 0, 0, 0
    def usar_habilidade_ativa(self, inimigo):
        # O Mago pode escolher um dos três poderes quando a recarga termina.
        while (True):
            if(self.carregamento_habilidade == 0):
                escolha = input("Desejar usar uma de suas habilidades? "
                                "1 - sim"
                                "2 - não")
                if(escolha == "1"):
                    habilidade = input("Qual habidade? \n"
                                    "1 - Raio paralisante \n"
                                    "2 - Double luck \n"
                                    "3 - Escudo imperfeito \n")
                    if(habilidade == "1"):
                        # O Raio Paralisante impede o monstro de agir neste turno.
                        inimigo.paralisado = True
                        self.carregamento_habilidade = 2
                        break
                    elif(habilidade == "2"):
                        # Double Luck permite rolar dois dados e usar o maior.
                        self.sortudo = True
                        self.carregamento_habilidade = 2
                        break
                    elif(habilidade == "3"):
                        # O escudo devolve ao inimigo metade do dano recebido.
                        self.escudo_imperfeito = True
                        self.carregamento_habilidade = 2
                        break
                    else:
                        print("Opção invalida!")
                elif(escolha == "2"):
                    break
                else:
                    print("Opção invalida!")
            else:
                # Enquanto recarrega, o Mago não pode escolher outro poder.
                print(f"A habilidade está carregando, faltam {self.carregamento_habilidade} para poder utilizar novamente")
                self.carregamento_habilidade -= 1
                break