import pygame

class Colours:
    WHITE = [255, 255, 255]
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    GREY = [128, 128, 128]
    

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("map testing")

clock = pygame.time.Clock()
        
player = pygame.Rect(370, 270, 30, 100)
#landscape1 = pygame.image.load("landscape1_11zon.jpeg")
#landscape2 = pygame.image.load("landscape2_11zon.jpeg")
c1_obstacle_1 = pygame.Rect(0, 0, 200, 100),
c1_obstacle_2 = pygame.Rect(300, 0, 500, 100)
cell_1_rects = [
    c1_obstacle_1,
    c1_obstacle_2
]

def cell_change_anim(x_pos, y_pos, col_1, col_2, image_1, image_2):
    time_count = 0
    fadeIn = pygame.Surface((800, 600)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill(Colours.BLACK)
    for i in range(0, 260, 5):
        if col_1 != 0:
            win.fill((col_1))
        else:
            win.blit(image_1, (0, 0))
        pygame.draw.rect(win, Colours.WHITE, player)
        fadeIn.set_alpha(i)
        win.blit(fadeIn, (0, 0))
        pygame.display.update()
        pygame.time.wait(5)
    player.y = y_pos
    fadeIn.set_alpha(0)

    fadeOut = pygame.Surface((800, 600)).convert_alpha()
    fadeOut.set_alpha(255)
    fadeOut.fill(Colours.BLACK)
    alpha = 255
    while alpha > 0:
        if col_2 != 0:
            win.fill((col_2))
        else:
            win.blit(image_2, (0, 0))
        pygame.draw.rect(win, Colours.WHITE, player)
        fadeOut.set_alpha(alpha)
        win.blit(fadeOut, (0, 0))
        pygame.display.update()
        pygame.time.wait(5)
        alpha -= 5



def game():
    colour = Colours.GREY
    stage = "main"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
         
        clock.tick(60)

        if keys[pygame.K_w] and player.top > 0:
            player.y -= 8
        elif keys[pygame.K_s] and player.bottom < 600:
            player.y += 8
        elif keys[pygame.K_a] and player.left > 0:
            player.x -= 8
        elif keys[pygame.K_d] and player.right < 800:
            player.x += 8
        
                
        win.fill((colour))
        pygame.draw.rect(win, Colours.WHITE, player)
#--------- CELL 1 SPECIFIC CODE -----------
        if stage == "main":
            colour = Colours.GREY
            if keys[pygame.K_w] and player.collideobjects(cell_1_rects):
                player.y += 8
            elif keys[pygame.K_s] and player.collideobjects(cell_1_rects):
                player.y -= 8
            elif keys[pygame.K_a] and player.collideobjects(cell_1_rects):
                player.x += 8
            elif keys[pygame.K_d] and player.collideobjects(cell_1_rects):
                player.x -= 8
            pygame.draw.rect(win, Colours.WHITE, c1_obstacle_1)
            pygame.draw.rect(win, Colours.WHITE, c1_obstacle_2)

#--------- CELL 2 SPECIFIC CODE -----------
        elif stage == "up":
            colour = Colours.BLUE
            
        if player.top < 0:
            x_coord = 0
            y_coord = 499
            cell_change_anim(x_coord, y_coord, colour, Colours.BLUE, 0, 0)
            if stage == "main":
                stage = "up"

        #win.fill((colour))
        pygame.display.update()

        

    pygame.quit()


def cell_2():
    colour = Colours.GREEN
    stage = "up"
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
         
        clock.tick(60)

        if keys[pygame.K_w] and player.top > 0:
            player.y -= 8
        elif keys[pygame.K_s] and player.bottom < 600:
            player.y += 8
        elif keys[pygame.K_a] and player.left > 0:
            player.x -= 8
        elif keys[pygame.K_d] and player.right < 800:
            player.x += 8

        win.blit(landscape2, (0, 0))

        pygame.draw.rect(win, Colours.WHITE, player)

        pygame.display.update()

    pygame.quit()


'''  if stage == "main":
        colour = Colours.RED
        if player.top < 0:
            stage = "up"
            player.y = 499
            cell_change_anim(Colours.GREEN, stage)
        elif player.left < 0:
            stage = "left"
            player.x = 770
    
    elif stage == "up":
        colour = Colours.GREEN
        if player.bottom > 600:
            stage = "main"
            player.y = 1
    elif stage == "left":
        colour = Colours.BLUE
        if player.right < 800:
            stage = "main"
            player.x = 1'''
            
game()






