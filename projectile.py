import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, facing_right):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("images/projectile.png")
        pos_y -= 7
        pos_x += 25

        if facing_right == True:
            self.image = image
            self.rect = self.image.get_rect(center=(pos_x, pos_y))
            self.direction = 5
        else:
            self.image = pygame.transform.flip(image, True, False)
            self.rect = self.image.get_rect(center=(pos_x, pos_y))
            self.direction = -5

    def update(self, shift):
        self.rect.x += shift
        self.rect.x += self.direction
