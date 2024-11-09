import pygame
from comet import Comet

#  On créer une classe pour gérer l'évènement à interval régulier
class CometFallEvent:

    # Lors du chargement on crée un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 12
        # on définit un groupe de sprite pour gérer les comètes
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    #  Méthode qui ajoute du pourcentage à la jauge
    def add_percent(self):
        self.percent += self.percent_speed / 100
    
    #  Méthode qui met à jour une barre
    def update_bar(self, surface):
        
        # On ajoute du pourcentage
        self.add_percent()

        # Arrière plan
        pygame.draw.rect(surface, (0,0,0), [
            0, # axe des x
            surface.get_height() - 20, # axe des y
            surface.get_width(), # longueur de la barre
            10 # épaisseur de la barre
        ])
        
        # barre de jauge
        pygame.draw.rect(surface, (187,11,11), [
            0, # axe des x
            surface.get_height() - 20, # axe des y
            (surface.get_width() / 100) * self.percent, # longueur de la barre en fonction du pourcentage de remplissage
            10 # épaisseur de la barre
        ])
    
    #  On vérifie si la jauge est à 100%
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # Boucle pour faire apparaître un nombre aléatoire de comète
        for i in range(1, 10):
            # On fait apparaître une comete
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True # On active l'évènement