import pygame


class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, size, code):
        super().__init__()

        if code == True:
            self.image = pygame.image.load(
                "C:/Users/tedri/Desktop/WizardGame/images/tile.png").convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        if code == False:
            self.image = pygame.image.load(
                "C:/Users/tedri/Desktop/WizardGame/images/end.png").convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
