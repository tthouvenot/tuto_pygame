import pygame
import random

# On crée la classe qui gère les animations

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f"./assests/{sprite_name}.png")
        # attribut pour savoir sur quelle image on est
        self.current_image = 0 # on commence à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # On définit une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # on défini une méthode pour animer le sprite
    def animate(self, loop = False):
        # On vérifie si l'animation est active
        if self.animation:
            
            if not loop:
                # passer à l'image suivante
                self.current_image += 2
            else:
                self.current_image += random.randint(0,1)

            # on vérifie si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # on remet l'animation au départ
                self.current_image = 0

                # On vérifie si l'animation n'est pas dans une boucle
                if not loop:
                    # On désactive l'animation
                    self.animation = False

            # on modifie l'image de l'animation précédente par la suivante
            self.image = self.images[self.current_image]

# on défini une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # on charge les 24 images du sprite
    images = []

    # on récupère le chemin du dossier
    path = f"./assests/{sprite_name}/{sprite_name}"

    # On boucle sur chaque image dans le dossier
    for number in range(1, 24):
        image_path = f"{path}{number}.png"
        images.append(pygame.image.load(image_path))

    # on renvoie le contenu de la liste d'image
    return images

# On défini un dictionnaire qui contient les images chargées de chaque sprite
# mummy -> [...mummy1.png,...]
animations = {
    'mummy': load_animation_images("mummy"),
    'player': load_animation_images("player")
}