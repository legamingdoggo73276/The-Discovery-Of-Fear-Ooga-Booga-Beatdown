import pygame

pygame.init()

#window size and heading: DO NOT MODIFY 
win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The Discovery Of Fear: Ooga Booga Beatdown")

running = True
while running:

    #for loop so the close button works: DO NOT MODIFY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#DO NOT DELETE
pygame.quit()