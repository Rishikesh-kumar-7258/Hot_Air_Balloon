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
        self.screen = None
        self.balloon = Balloon(x=100, y=500, screen=self.screen)
        self.all_sprites = pygame.sprite.Group()

        self.all_sprites.add(self.balloon)

    def render(self) -> None :
        # Write(text="This is playstate", fontsize=72, screen=self.screen)
        self.all_sprites.draw(self.screen)

    def update(self) -> None:
        self.balloon.update()
        self.render()
    
    def enter(self, **params):
        self.__init__()

        self.screen = params['screen']
        self.wwidth = params['width']
        self.wheight = params['height']
        self.gstatemachine = params['statemachine']
