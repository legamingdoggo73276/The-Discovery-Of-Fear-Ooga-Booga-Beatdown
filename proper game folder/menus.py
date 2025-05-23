
import pygame
from game import *
pygame.init()

# I dont actually know what this is doing since there is a near identical function in game.py, so keeping for now
def cell_change_anim(col_1, col_2):
    fadeIn = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill("black")
    for i in range(0, 260, 5):
        win.blit(fadeIn, (0, 0))
        fadeIn.set_alpha(i)
        pygame.display.update()
        pygame.time.wait(20)
    fadeIn.set_alpha(0)

    fadeOut = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeOut.set_alpha(255)
    fadeOut.fill("black")
    alpha = 255
    while alpha > 0:
        cell_1.blits(cell_1)
        fadeOut.set_alpha(alpha)
        win.blit(fadeOut, (0, 0))
        pygame.display.update()
        pygame.time.wait(20)
        alpha -= 5


