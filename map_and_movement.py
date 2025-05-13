import pygame

class Colours:
    WHITE = [255, 255, 255]
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    GREY = [128, 128, 128]
    
pygame.init()
window_height = 800
window_width = 1200

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("map testing")

clock = pygame.time.Clock()

arrow = pygame.image.load("arrow.png").convert_alpha()
rock = pygame.image.load("rock.png").convert_alpha()
arrow = pygame.transform.scale(arrow, (100, 100))
player = arrow.get_rect(center=(600, 400))

    

def cell_change_anim(x_pos, y_pos, c1, c2):
    fadeIn = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill(Colours.BLACK)
    for i in range(0, 260, 5):
        win.fill((c1.colour))
        win.blits(((c1.imgs[0], c1.rects[0]), (c1.imgs[1], c1.rects[1]), (arrow, player), (fadeIn, (0, 0))))
        fadeIn.set_alpha(i)
        pygame.display.update()
        pygame.time.wait(5)
    player.x = x_pos
    player.y = y_pos

    fadeOut = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeOut.fill(Colours.BLACK)
    alpha = 255
    while alpha > 0:
        win.fill((c2.colour))
        win.blits(((c2.imgs[0], c2.rects[0]), (c2.imgs[1], c2.rects[1]), (arrow, player), (fadeOut, (0, 0))))
        fadeOut.set_alpha(alpha)
        pygame.display.update()
        pygame.time.wait(5)
        alpha -= 5



class Map:
    img_1 = pygame.transform.scale(rock, (200, 100))
    img_2 = pygame.transform.scale(rock, (500, 100))
    obstacle_1 = img_1.get_rect(center=(300, 300))
    obstacle_2 = img_2.get_rect(center=(700, 700))
    colour = Colours.GREY
    stage = "main"
    running = True
    obstacles = [obstacle_1, obstacle_2]
    imgs = [img_1, img_2]
    combat_1 = False
                
    def __init__(self):
        if self.running == True:
            Map.game(Map.colour, Map.stage, Map.running)
            
    def combat_placeholder():
        if Map.combat_1 == False:
            print("whoa")
            Map.combat_1 = True
            
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
                if player.collideobjects(Map.obstacles):
                    player.y += 10
            elif keys[pygame.K_s] and player.bottom < window_height:
                player.y += 10
                if player.collideobjects(Map.obstacles):
                    player.y -= 10
            elif keys[pygame.K_a] and player.left > 0:
                player.x -= 10
                if player.collideobjects(Map.obstacles):
                    player.x += 10
            elif keys[pygame.K_d] and player.right < window_width:
                player.x += 10
                if player.collideobjects(Map.obstacles):
                    player.x -= 10
            

            win.fill((bg))
            win.blits(((Map.imgs[0], Map.obstacles[0]), (Map.imgs[1], Map.obstacles[1]), (arrow, player)))


            if cell == "main":
                if player.top <= 0:
                    cell_change_anim(player_x, (window_height - 101), cell_1, cell_2)
                    cell_2()
                elif player.bottom >= window_height:
                    cell_change_anim(player_x, 1, cell_1, cell_3)
                    cell_3()
                elif player.right >= window_width:
                    cell_change_anim(1, player_y, cell_1, cell_4)
                    cell_4()
                elif player.left <= 0:
                    cell_change_anim((window_width - 101), player_y, cell_1, cell_6)
                    cell_6()
            elif cell == "up":
                if player.bottom >= window_height:
                    cell_change_anim(player_x, 1, cell_2, cell_1)
                    cell_1()
            elif cell == "down":
                if player.top <= 0:
                    cell_change_anim(player_x, (window_height - 101), cell_3, cell_1)
                    cell_1()
            elif cell == "left":
                if player.right >= window_width:
                    cell_change_anim(1, player_y, cell_6, cell_1)
                    cell_1()
            elif cell == "right":
                if player.left <= 0:
                    cell_change_anim((window_width - 101), player_y, cell_4, cell_1)
                    cell_1()

            pygame.display.update()
                

        pygame.quit()

        
        
class cell_1(Map):
    img_1 = pygame.transform.scale(rock, (200, 100))
    img_2 = pygame.transform.scale(rock, (500, 100))
    obstacle_1 = img_1.get_rect(center=(300, 300))
    obstacle_2 = img_2.get_rect(center=(700, 700))
    colour = Colours.GREY
    stage = "main"
    rects = [obstacle_1, obstacle_2]
    imgs = [img_1, img_2]
    def __init__(self):
        Map.colour = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
class cell_2(Map):
    img_1 = pygame.transform.scale(rock, (100, 100))
    img_1 = pygame.transform.scale(rock, (300, 100))
    obstacle_1 = img_1.get_rect(center=(100, 100))
    obstacle_2 = img_1.get_rect(center=(500, 500))
    colour = "pink"
    stage = "up"
    rects = [obstacle_1, obstacle_2]
    imgs = [img_1, img_2]
    def __init__(self):
        Map.combat_placeholder()
        Map.colour = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
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
    
        
Map()

