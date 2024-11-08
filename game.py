import pygame
# On importe la classe player
from player import Player
# On importe le monstre
from monster import Monster

# On crée la classe qui représente le jeu
class Game:

    def __init__(self):
        # Défini si le jeu a commencé ou pas
        self.is_playing = False
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
      

    # On va gérer les collisions
    def check_collision(self, sprite, group):
        # Méthode spécifique à pygame on compare notre sprite à un groupe, on indique s'il meurt ou pas et enfin le comportement
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # On crée une méthode pour faire spawn les monstres
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    # On crée la méthode de mise à jour des composants
    def update(self, screen):
        # On actualise la barre de jeu du joueur
        self.player.update_health_bar(screen)

        # On applique l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # On récupère les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # On récupère tous les monstres pour les bouger
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # On applique l'ensemble des images du groupe du projectile
        self.player.all_projectiles.draw(screen)

        # On applique l'ensemble des images du groupe monstres
        self.all_monsters.draw(screen)

        # On vérifie si la touche est appuyée
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()

    # On gère le game over
    def game_over(self):
        # On remet le jeu à neuf, on retire les monstres, remettre le joueur à 100 de vie et le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def start(self):
        self.is_playing = True
          # Au démarrage on fait spanw immédiatement le monstre
        self.spawn_monster()
        self.spawn_monster()
