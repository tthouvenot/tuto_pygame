import pygame
from projectile import Projectile

# On créé la classe du joueur. Elle hérite de la classe Sprite du module sprite de pygame
class Player(pygame.sprite.Sprite):

    # On passe l'instance du jeu en paramètre pour l'avoir en attribut
    def __init__(self, game):
        # On initialise la classe parent
        super().__init__()
        self.game = game
        # On définie les attributs
        self.health = 100 # Points de vie actuel
        self.max_health = 100 # Points de vie initial
        self.attack = 10
        self.velocity = 5
        # On crée un groupe de projectile
        self.all_projectiles = pygame.sprite.Group()
        # On définie le sprite qui représente le joueur
        self.image = pygame.image.load("./assests/player.png")
        # On génère et stock la représentation rectangulaire du joueur
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        # Permet d'avoir une vélocity inférieur à 1
        self.position_x = float(self.rect.x)

    # On défini la méthode de lancement de la boule de feu
    def launch_projectile(self):
        # On crée l'instance du projectile et on l'ajoute au groupe. On passe en argument le joueur lui même
        self.all_projectiles.add(Projectile(self))

    # On crée les méthode de déplacement
    def move_right(self):
        # On peut se déplacer que si le joueur n'entre pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.position_x += self.velocity
            self.rect.x = int(self.position_x)
    def move_left(self):
        self.position_x -= self.velocity
        self.rect.x = int(self.position_x)
