import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.velocity = random.randint(1,3)
        self.image = pygame.image.load('./assests/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.position_x = float(self.rect.x)

    def damage(self, amount):
        # on inflige des dégâts
        self.health -= amount

        # On vérifie si le nombre de pv est inférieur ou égale à 0
        if self.health <= 0:
            # On supprime ou on le fait réapparaître comme nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.position_x = float(self.rect.x)
            self.health = self.max_health
            self.velocity = random.randint(1,3)

    def update_health_bar(self, surface):

        # On dessine les barres de vie (surface, couleur, position). Attention la position a son importance 
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 15, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x + 15, self.rect.y - 20, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.position_x -= self.velocity
            self.rect.x = int(self.position_x)

        # Si le monstre est en collision avec le joueur
        else:
            # On inflige des dégâts
            self.game.player.damage(self.attack)