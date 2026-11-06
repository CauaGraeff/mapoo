from Cavaleiro import Cavaleiro
from Inimigos import Inimigos, Goblin
from BatalhaManager import BatalhaManager

cavaleiro = Cavaleiro("Josué")
goblin = Goblin()

teste = BatalhaManager(cavaleiro, goblin)

teste.executar_turno()

