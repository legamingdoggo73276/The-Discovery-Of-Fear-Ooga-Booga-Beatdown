import pygame
from game import *
pygame.init()

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Main Menu")

font = pygame.font.Font("who-asks-satan.ttf", 40)
surf = font.render("Quit", True, "red")
surf2 = font.render("Start", True, "red")
image1 = pygame.image.load("images/button.png").convert_alpha()
image2 = pygame.transform.scale(image1, (100, 60))
image1 = pygame.transform.scale(image1, (80, 60))

button = image1.get_rect()
button2 = image2.get_rect()
button.center = (200, 200)
button2.center = (200, 500)

bg = (69, 69, 69)

def cell_change_anim(col_1, col_2):
    fadeIn = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill("black")
    for i in range(0, 260, 5):
        blits()
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


def blits():
    win.blits(((image1, (button.x, button.y)), (image2, (button2.x, button2.y)), (surf, (button.x +10, button.y + 5)), (surf2, (button2.x +10, button2.y +5))))

while True:
    win.fill(bg)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                pygame.quit()
            elif button2.collidepoint(events.pos):
                cell_change_anim("pink", "grey")
                Map()
                bg = ("grey")
                
        a, b = pygame.mouse.get_pos()
        if button.x <= a <= button.x + 100 and button.y <= b <= button.y +60:
            image1.set_alpha(210)
            surf.set_alpha(210)
        else:
            image1.set_alpha(255)
            surf.set_alpha(255)
        if button2.x <= a <= button2.x + 110 and button2.y <= b <= button2.y +60:
            image2.set_alpha(210)
            surf2.set_alpha(210)
        else:
            image2.set_alpha(255)
            surf2.set_alpha(255)
        
        
        blits()
        pygame.display.update()
