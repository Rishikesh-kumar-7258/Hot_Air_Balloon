from Classes.hurdles import Hurdle
from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN, KEYUP
from pygame.color import THECOLORS
from Classes.balloon import Balloon
from Utils.functions import Write
import pygame
from States.basestate import Base
from random import *

class Play(Base):
    """
    This is play state, the actual playground of our game.
    """

    def __init__(self) -> None:
        super().__init__()

        self.speedY = 2
        self.speedX = 0

        self.hurdle_speed = 5
        self.countDeleted = 0
        self.score = 0


    def render(self) -> None :
        Write(text=f"Score : {self.score}", fontsize=25, screen=self.screen, color=THECOLORS['goldenrod'])
        self.all_sprites.draw(self.screen)

    def update(self, params) -> None:

        if self.current_hurdle.rect.y > 200 : 
            self.current_hurdle = Hurdle()
            self.current_hurdle.rect.center = (randrange(self.current_hurdle.rect.width, self.wwidth - self.current_hurdle.rect.width), 0)
            self.all_sprites.add(self.current_hurdle)
            self.hurdles.add(self.current_hurdle)

        passedCount = 0
        for hurdle in self.hurdles:
            if pygame.sprite.collide_mask(self.balloon, hurdle):
                self.speedY = 0
                self.hurdle_speed = 0
                self.gstatemachine.change("over", screen=self.screen, width=self.wwidth, height=self.wheight, score=self.score, gstatemachine=self.gstatemachine)
            hurdle.rect.y += self.hurdle_speed

            if hurdle.rect.y > self.balloon.rect.y + self.balloon.rect.height:
                passedCount += 1
                self.hurdle_speed += 0.01

            if hurdle.rect.y >= self.wheight : 
                self.countDeleted += 1
                hurdle.kill()
            
        self.score = self.countDeleted + passedCount


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
        self.hurdles = pygame.sprite.Group()

        self.all_sprites.add(self.balloon)

        self.current_hurdle = Hurdle()
        self.current_hurdle.rect.center = (randrange(self.current_hurdle.rect.width, self.wwidth - self.current_hurdle.rect.width), 0)
        self.all_sprites.add(self.current_hurdle)
        self.hurdles.add(self.current_hurdle)
