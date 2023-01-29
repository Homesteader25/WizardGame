import pygame


class projectile(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("images/projectile.png")
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
