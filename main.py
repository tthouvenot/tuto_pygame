import math
# On import le module et on l'initialise
import pygame
pygame.init()

# On importe la classe Game
from game import Game

# On génère la fenêtre du jeu
pygame.display.set_caption("Mon premier Jeu")
screen = pygame.display.set_mode((1080,720)) #Renvoie une surface

# On défini le framerate
clock = pygame.time.Clock()

# On importe le background
background = pygame.image.load("./assests/bg.jpg")

# On charge la bannière
banner = pygame.image.load("./assests/banner.png")  
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# On importe le bouton pour démarrer la partie
play_button = pygame.image.load('./assests/button.png') 
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33 + 10)
play_button_rect.y = math.ceil(screen.get_height() / 2 + 10)

# On charge l'instance du jeu
game = Game()

# Boucle de jeu tant que running est vrai 
running = True
while running:

    # Applique l'arrière plan du jeu (image, (positionX les abscisses , positionY les ordonnées)). IMPORTANT: le point d'origine (0,0) est en haut à gauche
    screen.blit(background, (0,-200))
    
    # On vérifie si le jeu a commencé
    if game.is_playing:
        # On déclenche les instructions de la partie
        game.update(screen)    
    # On vérifie si le jeu n'a pas commencé
    else:
        # On ajoute l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # On met à jour l'écran
    pygame.display.flip()

    # On applique le 60 fps
    clock.tick(60)

    for event in pygame.event.get():

        # On vérifie tous les évènements pour gérer la fermeture de la fenêtre
        # On quitte le jeu
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # On détécte les touches du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # On détecte si la touche espace est appuyée
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    game.start()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        # on vérifie si on clique sur le bouton play avec la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # On vérifie si on a la souris sur le bouton play
            if play_button_rect.collidepoint(event.pos):
                # On met le jeu en mode lancer
                game.start()
                # jouer le son
                game.sound_manager.play('click')