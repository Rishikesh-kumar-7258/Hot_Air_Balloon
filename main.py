import pygame
from Classes.statemachine import StateMachine
from States.startstate import Start
import sys
from pygame.constants import QUIT
from pygame.color import THECOLORS

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
GAME_OVER = False
clock = pygame.time.Clock()

STATES = {
    "start" : Start()
}

gstatemachine = StateMachine(STATES)
gstatemachine.change("start", 
                            screen = SCREEN)

while not GAME_OVER:

    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_OVER = True

    SCREEN.fill(THECOLORS["black"])
    gstatemachine.update()
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
sys.exit()