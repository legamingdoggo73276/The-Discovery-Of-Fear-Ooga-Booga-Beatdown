import pygame
from fight import battle
import stats
from healthbar import *
pygame.font.init()
pygame.init()

result = battle("Mole Rat", 5, 50, playerStr, playerHP, playerSpeed, 10)

clock = pygame.time.Clock()

#window size and heading: DO NOT MODIFY 
font = pygame.font.Font("who-asks-satan.ttf", 40)
win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The Discovery Of Fear: Ooga Booga Beatdown")
molerat = pygame.image.load("images/molerat.png").convert_alpha()
molerat = pygame.transform.scale(molerat, (1200, 800))

running = True
while running:

    #for loop so the close button works: DO NOT MODIFY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)
    win.fill((69, 69, 69))

    #text_surface = font.render(result , False, (255, 255, 255))

    health_bar.hp = stats.playerHP
    health_bar.draw(win)

    #win.blit(molerat, (0,0))
    win.blit(heart,(950,5))

    pygame.display.update()
#DO NOT DELETE
pygame.quit()
