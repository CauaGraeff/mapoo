from Cavaleiro import Cavaleiro
from Inimigos import Inimigos, Goblin
from BatalhaManager import BatalhaManager
from Mago import Mago

cavaleiro = Mago("Josué")
goblin = Goblin()

teste = BatalhaManager(cavaleiro, goblin)

teste.executar_turno()