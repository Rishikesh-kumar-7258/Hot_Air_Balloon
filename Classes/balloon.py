import pygame
from pygame.color import THECOLORS

class Balloon(pygame.sprite.Sprite):
    
    def __init__(self, x=0, y=0, screen=None) -> None:
        super().__init__()

        self.x = x
        self.y = y
        self.screen = screen
        
        self.image1 = pygame.image.load("Utils/Images/straight.png").convert()
        self.image2 = pygame.image.load("Utils/Images/left.png").convert()
        self.image3 = pygame.image.load("Utils/Images/right.png").convert()

        self.image = self.image1
        self.image.set_colorkey(THECOLORS['white'])
        self.rect = self.image.get_rect()

        self.rect.center = (self.x, self.y)

        self.mask = pygame.mask.from_surface(self.image)
    
    def change(self, orient=None):
        if orient == "left": 
            self.image = self.image2
            self.image.set_colorkey(THECOLORS['white'])
        elif orient == 'right':
            self.image = self.image3
            self.image.set_colorkey(THECOLORS['white'])
        else : 
            self.image = self.image1
            self.image.set_colorkey(THECOLORS['white'])