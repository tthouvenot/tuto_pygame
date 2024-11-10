import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.position_x = float(self.rect.x)
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1,3)
        

    def damage(self, amount):
        # on inflige des dégâts
        self.health -= amount

        # On vérifie si le nombre de pv est inférieur ou égale à 0
        if self.health <= 0:
            # On supprime ou on le fait réapparaître comme nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.position_x = float(self.rect.x)
            self.health = self.max_health
            self.velocity = random.randint(1,self.default_speed)

        # Si la barre d'évènement est chargée au max
        if self.game.comet_event.is_full_loaded():
            self.game.all_monsters.remove(self)

            # On appel la méthode pour déclancher la pluie de comète
            self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

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

# on définit une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)

# On définit une classe pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300,300), 130)
        self.health = 250
        self.max_health = 250
        self.set_speed(1)
        self.attack = 0.8