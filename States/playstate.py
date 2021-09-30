from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN, KEYUP
from Classes.balloon import Balloon
from Utils.functions import Write
import pygame
from States.basestate import Base

class Play(Base):
    """
    This is play state, the actual playground of our game.
    """

    def __init__(self) -> None:
        super().__init__()

        self.speedY = 2
        self.speedX = 0


    def render(self) -> None :
        # Write(text="This is playstate", fontsize=72, screen=self.screen)
        self.all_sprites.draw(self.screen)

    def update(self, params) -> None:

        if self.balloon.rect.y > self.wwidth // 2 + 100: self.balloon.rect.y -= self.speedY
        if self.balloon.rect.left >= 0 and self.balloon.rect.right <= self.wwidth : self.balloon.rect.x += self.speedX
        if self.balloon.rect.left <= 0 : self.balloon.rect.left = 2
        if self.balloon.rect.right >= self.wwidth : self.balloon.rect.right = self.wwidth - 2

        for event in params:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.balloon.change("left")
                    self.speedX = -5
                if event.key == K_RIGHT:
                    self.balloon.change("right")
                    self.speedX = 5
            
            if event.type == KEYUP:
                self.balloon.change()
                self.speedX = 0
        
        self.balloon.update()
        self.render()
    
    def enter(self, **params):
        self.__init__()

        self.screen = params['screen']
        self.wwidth = params['width']
        self.wheight = params['height']
        self.gstatemachine = params['statemachine']

        self.balloon = Balloon(x=self.wwidth // 2, y=self.wheight - 50, screen=self.screen)
        self.all_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.balloon)
