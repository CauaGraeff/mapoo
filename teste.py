"""Exemplo pequeno que começa uma luta entre um Paladino e um Goblin."""

# Importa as peças que serão usadas neste teste.
from Cavaleiro import Cavaleiro
from Inimigos import Inimigos, Goblin
from BatalhaManager import BatalhaManager
from Mago import Mago
from Paladino import Paladino

# Cria os dois lutadores.
cavaleiro = Cavaleiro("cavaleiro")
goblin = Goblin()

# Prepara a batalha com o herói e o monstro.
teste = BatalhaManager(cavaleiro, goblin)

# Começa os turnos até que alguém vença.
teste.executar_turno()