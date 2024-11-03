import pygame
# On importe la classe player
from player import Player
# On importe le monstre
from monster import Monster

# On crée la classe qui représente le jeu
class Game:

    def __init__(self):
        # On crée le groupe de sprite représentant le joueur
        self.all_players = pygame.sprite.Group()
        # On génère l'instance du joueur
        self.player = Player(self)
        # On ajoute le joueur au groupe de sprite
        self.all_players.add(self.player)
        # On gère les touches actives
        self.pressed = {}
        # On crée un groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # Au démarrage on fait spanw immédiatement le monstre
        self.spawn_monster()
        self.spawn_monster()

    # On va gérer les collisions
    def check_collision(self, sprite, group):
        # Méthode spécifique à pygame on compare notre sprite à un groupe, on indique s'il meurt ou pas et enfin le comportement
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # On crée une méthode pour faire spawn les monstres
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)