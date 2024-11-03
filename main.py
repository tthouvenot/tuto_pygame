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
background = pygame.image.load(("./assests/bg.jpg"))

# On charge l'instance du jeu
game = Game()

# Boucle de jeu tant que running est vrai
running = True
while running:

    # Applique l'arrière plan du jeu (image, (positionX les abscisses , positionY les ordonnées)). IMPORTANT: le point d'origine (0,0) est en haut à gauche
    screen.blit(background, (0,-200))

    # On actualise la barre de jeu du joueur
    game.player.update_health_bar(screen)

    # On applique l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # On récupère les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # On récupère tous les monstres pour les bouger
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # On applique l'ensemble des images du groupe du projectile
    game.player.all_projectiles.draw(screen)

    # On applique l'ensemble des images du groupe monstres
    game.all_monsters.draw(screen)

    # On vérifie si la touche est appuyée
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

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
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        