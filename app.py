import pygame
from fight import battle
from stats import *
from healthbar import *
pygame.font.init()
pygame.init()

result = battle("ghoul", 5, 50, playerStr, playerHP, playerSpeed, 10)

clock = pygame.time.Clock()

#window size and heading: DO NOT MODIFY 
font = pygame.font.SysFont('Comic Sans MS', 30)
win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The Discovery Of Fear: Ooga Booga Beatdown")


running = True
while running:

    #for loop so the close button works: DO NOT MODIFY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)
    win.fill((69, 69, 69))

    text_surface = font.render(result , False, (255, 255, 255))
    health_bar.hp = playerHP
    health_bar.draw(win)
    win.blits(((text_surface, (600,400)), (heart,(950,5))))

    win.blit(text_surface, (300,200))


    pygame.display.update()
#DO NOT DELETE
pygame.quit()