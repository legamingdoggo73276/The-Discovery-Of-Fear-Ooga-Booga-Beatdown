import pygame
from game import *
from fight import battle
import stats
from healthbar import *
#from menus import *
from audio import *
pygame.font.init()
pygame.init()

clock = pygame.time.Clock()

#window size and heading: DO NOT MODIFY 
win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The Discovery Of Fear: Ooga Booga Beatdown")
molerat = pygame.image.load("images/molerat.png").convert_alpha()
molerat = pygame.transform.scale(molerat, (1200, 800))
font = pygame.font.Font("PanicStricken.ttf", 50)
surf = font.render("Quit", True, "red")
surf2 = font.render("Start", True, "red")
button = pygame.image.load("images/button.png").convert_alpha()
start = pygame.image.load("images/start.png").convert_alpha()
image1 = pygame.transform.scale(button, (125, 75))
image2 = pygame.transform.scale(button, (144, 75))
start = pygame.transform.scale(start, (1200, 800))

buttonaudio = pygame.mixer.Sound(sound_collection[0])
menumusic = music_collection[0]
#call menu music before main loop
music(menumusic)

button = image1.get_rect()
button2 = image2.get_rect()
button.center = (900, 650)
button2.center = (300, 650)

def blits():
    win.blits(((start, (0, 0)), (image1, (button.x, button.y)), (image2, (button2.x, button2.y)), (surf, (button.x +10, button.y + 5)), (surf2, (button2.x +10, button2.y +5))))

def starting_fade():
    fadeIn = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill("black")
    for i in range(0, 260, 5):
        win.blit(fadeIn, (0, 0))
        fadeIn.set_alpha(i)
        pygame.display.update()
        pygame.time.wait(40)

    fadeOut = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeOut.fill("black")
    alpha = 255
    while alpha > 0:
        starting_cell.blits(starting_cell)
        fadeOut.set_alpha(alpha)
        win.blit(fadeOut, (0, 0))
        pygame.display.update()
        pygame.time.wait(30)
        alpha -= 5


running = True
while running:
        #for loop so the close button works: DO NOT MODIFY  
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            if events.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(events.pos):
                    sound(buttonaudio)
                    pygame.time.wait(400)
                    pygame.quit()
                elif button2.collidepoint(events.pos):
                    sound(buttonaudio)
                    pygame.mixer.music.fadeout(1000)
                    starting_fade()
                    Map()
            
            clock.tick(60)

            health_bar.hp = Stats.playerHP
            health_bar.draw(win)

            win.blit(heart,(950,5))

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
            def blits():
                win.blits(((start, (0, 0)), (image1, (button.x, button.y)), (image2, (button2.x, button2.y)), (surf, (button.x +10, button.y + 5)), (surf2, (button2.x +10, button2.y +5))))

            pygame.display.update()