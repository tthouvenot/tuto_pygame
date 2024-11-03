# On importe la classe player
from player import Player

# On crée la classe qui représente le jeu
class Game:

    def __init__(self):
        # On génère l'instance du joueur
        self.player = Player()
        # On gère les touches actives
        self.pressed = {}