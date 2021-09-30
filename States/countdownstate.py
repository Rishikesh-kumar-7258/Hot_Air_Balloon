import pygame
from States.basestate import Base
from Utils.functions import Write
from pygame.color import THECOLORS

class Countdown(Base):
    """
    This is the countdown state. It will reverse count from 3 to 0. When it hits 0 the state will change 
    to play state.
    """

    def __init__(self) -> None:
        super().__init__()

        self.count = 240

    def render(self)-> None :
        Write(fontsize=72, text=str(self.count//60), color=THECOLORS['goldenrod'], screen=self.screen, x=self.wwidth//2, y=self.wheight//2, center=True)
        Write(fontsize=24, text="use arrow keys left and right to move", color=THECOLORS['aquamarine'], screen=self.screen, x=self.wwidth//2, y=self.wheight//2 + 100, center=True)

    def update(self) -> None :
        self.count -= 1
        self.render()
        if self.count//60 <= 0 : self.gstatemachine.change('play', screen=self.screen, width=self.wwidth, height=self.wheight, statemachine=self.gstatemachine)
    
    def enter(self, **params):
        self.screen = params['screen']
        self.wwidth = params['width']
        self.wheight = params['height']
        self.gstatemachine = params['statemachine']

        self.__init__()