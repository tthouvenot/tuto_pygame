import pygame
import random

# On crée la classe de la comète
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # On défini l'image
        self.image = pygame.image.load('./assests/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 8)
        self.rect.x = random.randint(30, 1050)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event
        self.attack = 20

    #  Permet de gérer la chute de la comète
    def fall(self):
        self.rect.y += self.velocity
        # on joue le son
        self.comet_event.game.sound_manager.play('meteorite')

        # ne tombe pas sur le sol, si c'est le cas on la détruit
        if self.rect.y >= 500:
            self.remove()

            #  s'il n'y a plus de comète
            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False


        # on vérifie si la comète touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(self.attack)

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #  On vérifie s'il y a encore des comètes
        if len(self.comet_event.all_comets) == 0:
            # On remet la barre à 0
            self.comet_event.reset_percent()
            # On fait apparaître les monstres
            self.comet_event.game.start()