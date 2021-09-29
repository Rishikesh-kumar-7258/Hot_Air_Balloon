import pygame

def Write(fnt="Comic sans MS", fontsize=24, text="Namastey!", color=(255, 255, 255), background=None, screen=None):
    """
    This funtion will write the text on the screen. 
    It takes as arguments:
        font
        fontsize
        text
        color
        background
        screen
    """

    f = pygame.font.SysFont("Comis sans MS", fontsize)
    t = f.render(text, True, color, background)
    textRect = t.get_rect()
    screen.blit(t, textRect)
