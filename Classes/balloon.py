import pygame
from pygame.color import THECOLORS

class Balloon(pygame.sprite.Sprite):
    
    def __init__(self, x=0, y=0, screen=None) -> None:
        super().__init__()

        self.x = x
        self.y = y
        self.screen = screen
        
        self.image = pygame.image.load("Utils/Images/straight.png").convert()
        self.image.set_colorkey(THECOLORS['white'])
        self.rect = self.image.get_rect()

        self.rect.center = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)