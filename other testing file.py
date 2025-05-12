import pygame

class Colours:
    WHITE = [255, 255, 255]
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    GREY = [128, 128, 128]
#class Structure:
    

pygame.init()
window_height = 800
window_width = 1200

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("map testing")

clock = pygame.time.Clock()

arrow = pygame.image.load("arrow.png").convert_alpha()
rock = pygame.image.load("rock.png").convert_alpha()
arrow = pygame.transform.scale(arrow, (100, 100))
player = arrow.get_rect()
player.center = ((window_width/2), (window_height/2))

thingy_1 = pygame.transform.scale(rock, (200, 100))
thingy_2 = pygame.transform.scale(rock, (500, 100))
obstacle = thingy_1.get_rect()
obstacle.center = ((300, 300))
obstacle_2 = thingy_2.get_rect()
obstacle_2.center = ((500, 500))

cell_1_rects = [[thingy_1, obstacle],
                [thingy_2, obstacle_2]]
c1_obstacle_1 = pygame.Rect(0, 0, 200, 100),
c1_obstacle_2 = pygame.Rect(300, 0, 500, 100)
cell_1_rects = [
    c1_obstacle_1,
    c1_obstacle_2
]

def cell_change_anim(x_pos, y_pos, col_1, col_2, image_1, image_2):
    
    fadeIn = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill(Colours.BLACK)
    for i in range(0, 260, 5):
        if col_1 != 0:
            win.fill((col_1))
        else:
            win.blit(image_1, (0, 0))
        win.blit(arrow, player)
        fadeIn.set_alpha(i)
        win.blit(fadeIn, (0, 0))
        pygame.display.update()
        pygame.time.wait(5)
    player.x = x_pos
    player.y = y_pos

    fadeOut = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeOut.set_alpha(255)
    fadeOut.fill(Colours.BLACK)
    alpha = 255
    while alpha > 0:
        if col_2 != 0:
            win.fill((col_2))
        else:
            win.blit(image_2, (0, 0))
        win.blit(arrow, player)
        fadeOut.set_alpha(alpha)
        win.blit(fadeOut, (0, 0))
        pygame.display.update()
        pygame.time.wait(5)
        alpha -= 5


class Map:
    colour = Colours.GREY
    stage = "main"
    running = True
    obstacle = thingy_1
    obstacle_2 = thingy_2
    
    def combat_placeholder():
            done = False
            if done == False:
                print("whoa")
                done = True

                
    def __init__(self):
        if self.running == True:
            Map.game(Map.colour, Map.stage, Map.running)
            
    def game(bg, cell, run):
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            player_x = player.x
            player_y = player.y
            keys = pygame.key.get_pressed()
                 
            clock.tick(60)

            if keys[pygame.K_w] and player.top > 0:
                player.y -= 10
                if player.colliderect(obstacle):
                    player.y += 10

            elif keys[pygame.K_s] and player.bottom < window_height:
                player.y += 10
                if player.colliderect(obstacle):
                    player.y -= 10
            elif keys[pygame.K_a] and player.left > 0:
                player.x -= 10
                if player.colliderect(obstacle):
                    player.x += 10
            elif keys[pygame.K_d] and player.right < window_width:
                player.x += 10
                if player.colliderect(obstacle):
                    player.x -= 10
            

            win.fill((bg))
            win.blit(arrow, player)
            

            if cell == "main":
                win.blit(blit_sequence=((thingy_1, obstacle), (thingy_2, obstacle_2)))
                if player.top <= 0:
                    cell_change_anim(player_x, (window_height - 101), bg, cell_2.colour, 0, 0)
                    cell_2()
                elif player.bottom >= window_height:
                    cell_change_anim(player_x, 1, bg, cell_3.colour, 0, 0)
                    cell_3()
                elif player.right >= window_width:
                    cell_change_anim(1, player_y, bg, cell_4.colour, 0, 0)
                    cell_4()
                elif player.left <= 0:
                    cell_change_anim((window_width - 101), player_y, bg, cell_6.colour, 0, 0)
                    cell_6()
            elif cell == "up":
                if player.bottom >= window_height:
                    cell_change_anim(player_x, 1, bg, cell_1.colour, 0, 0)
                    cell_1()
            elif cell == "down":
                if player.top <= 0:
                    cell_change_anim(player_x, (window_height - 101), bg, cell_1.colour, 0, 0)
                    cell_1()
            elif cell == "left":
                if player.right >= window_width:
                    cell_change_anim(1, player_y, bg, cell_1.colour, 0, 0)
                    cell_1()
            elif cell == "right":
                if player.left <= 0:
                    cell_change_anim((window_width - 101), player_y, bg, cell_1.colour, 0, 0)
                    cell_1()

            pygame.display.update()
                

        pygame.quit()

        
        
class cell_1(Map):
    colour = Colours.GREY
    stage = "main"
    def __init__(self):
        Map.colour = self.colour
        Map.stage = self.stage
        
        Map()
class cell_2(Map):
    colour = "pink"
    stage = "up"
    Map.combat_placeholder()
    def __init__(self):
        Map.colour = self.colour
        Map.stage = self.stage
        Map()
class cell_3(Map):
    colour = "blue"
    stage = "down"
    def __init__(self):
        Map.colour = self.colour
        Map.stage = self.stage
        Map()
class cell_4(Map):
    colour = "orange"
    stage = "right"
    def __init__(self):
        Map.colour = self.colour
        Map.stage = self.stage
        Map()
class cell_5(Map):
    colour = "orange"
    stage = "up-right"
    def __init__(self):
        Map.colour = self.colour
        Map.stage = self.stage
        Map()
class cell_6(Map):
    colour = "purple"
    stage = "left"
    def __init__(self):
        Map.colour = self.colour
        Map.stage = self.stage
        Map()
    
        
            
    
            
            
'''    def game(bg, cell, run):
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()
                 
            clock.tick(60)

            if keys[pygame.K_w] and player.top > 0:
                player.y -= 5
            elif keys[pygame.K_s] and player.bottom < window_height:
                player.y += 5
            elif keys[pygame.K_a] and player.left > 0:
                player.x -= 5
            elif keys[pygame.K_d] and player.right < window_width:
                player.x += 5
            

            win.fill((bg))
            #pygame.draw.rect(win, Colours.WHITE, player)
            win.blit(arrow, player)
            pygame.display.update()
            #pygame.draw.

            if player.top <= 0:
                if cell == "main":
                    cell_change_anim(0, (window_height - 101), bg, "pink", 0, 0)
                    Map.cell_2(Map)
                if cell == "down":
                    cell_change_anim(0, (window_height - 101), bg, Map.cell_1().colour, 0, 0)
                    Map.cell_1(Map)
                #elif cell == "up":
                    
            elif player.bottom >= window_height+1:
                if cell == "up":
                    cell_change_anim(0, 1, bg, Colours.GREY, 0, 0)
                    Map.cell_1(Map)
                elif cell == "main":
                    cell_change_anim(0, 1, bg, "blue", 0, 0)
                    Map.cell_3()
            #elif player.right 

        pygame.quit()'''

Map()

    
    
'''def game():
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
            colour = Colours.GREEN
            
        if player.top < 0:
            x_coord = 0
            y_coord = 499
            cell_change_anim(x_coord, y_coord, colour, Colours.GREEN, 0, 0)
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


  if stage == "main":
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

            






