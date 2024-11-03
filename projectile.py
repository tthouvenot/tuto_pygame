import pygame

# On défini la classe qui gère le projectile
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.image = pygame.image.load("./assests/projectile.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        # On défini la position selon la position du joueur
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.position_x = self.rect.x
        # Important de garder l'image de base
        self.origin_image = self.image
        # Valeur de l'angle pour tourner le projectile
        self.angle = 0

    # On défini une méthode pour l'animation
    def rotate(self):
        self.angle += 12
        # On applique la rotation (le sprite concerné, l'angle de rotation, et le scale)
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        # On modifie le point d'origine des animations
        self.rect = self.image.get_rect(center=self.rect.center)

    # On défini une méthode pour détruire le projectile
    def remove(self):
        self.player.all_projectiles.remove(self)
        self.rotate()
    
    # On défini la méthode de déplacement
    def move(self):
        self.position_x += self.velocity
        self.rect.x = int(self.position_x)

        # On vérifie si le projectile entre en collision avec un monstre
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()

        # On vérifie si le projectile n'est plus sur l'écran
        if self.rect.x > 1080:
            # On supprime le projectile
            self.remove()