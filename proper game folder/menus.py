import pygame
pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("pygame button")

font = pygame.font.Font("who-asks-satan.ttf", 40)
#font.set_italic(True)
surf = font.render("Quit", True, "white")
surf2 = font.render("thingy", True, "white")
arrow = pygame.image.load("arrow_2.PNG").convert_alpha()
arrow = pygame.transform.scale(arrow, (100, 100))
image1 = pygame.image.load("button.png").convert_alpha()
image2 = pygame.transform.scale(image1, (160, 60))
image1 = pygame.transform.scale(image1, (110, 60))

button = image1.get_rect()
button2 = image2.get_rect()
button.center = (200, 200)
button2.center = (200, 500)

bg = "pink"

def cell_change_anim(col_1, col_2):
    time_count = 0
    fadeIn = pygame.Surface((800, 600)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill("black")
    for i in range(0, 260, 5):
        if col_1 != 0:
            win.fill((col_1))
        else:
            win.blit(image_1, (0, 0))
        #pygame.draw.rect(win, Colours.WHITE, player)
        fadeIn.set_alpha(i)
        win.blit(fadeIn, (0, 0))
        pygame.display.update()
        pygame.time.wait(10)
    #player.y = y_pos
    fadeIn.set_alpha(0)

    fadeOut = pygame.Surface((800, 600)).convert_alpha()
    fadeOut.set_alpha(255)
    fadeOut.fill("black")
    alpha = 255
    while alpha > 0:
        if col_2 != 0:
            win.fill((col_2))
        else:
            win.blit(image_2, (0, 0))
        #pygame.draw.rect(win, Colours.WHITE, player)
        fadeOut.set_alpha(alpha)
        win.blit(fadeOut, (0, 0))
        pygame.display.update()
        pygame.time.wait(10)
        alpha -= 5


        
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
        
        
        
        win.blit(image1, (button.x, button.y))
        win.blit(image2, (button2.x, button2.y))
        win.blit(surf, (button.x +10, button.y + 5))
        win.blit(surf2, (button2.x +10, button2.y +5))
        win.blit(arrow, (100, 100))

        pygame.display.update()
