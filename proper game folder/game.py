import pygame
from fight import battle
import stats
from healthbar import *

#colours for later use, probably removed when game is done
class Colours:
    WHITE = [255, 255, 255]
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    GREY = [128, 128, 128]

#init code, required
pygame.init()
window_height = 800
window_width = 1200
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("map testing")
clock = pygame.time.Clock()

#loading images and creating player
floor1 = pygame.image.load("images/mainfloor.png").convert_alpha()
cave2 = pygame.image.load("images/cave2.png").convert_alpha()
player = pygame.image.load("images/caveman.png").convert_alpha()
back = pygame.image.load("images/back.png").convert_alpha()
fire = pygame.image.load("images/fire.png").convert_alpha()
rock = pygame.image.load("images/rock.png").convert_alpha()
end = pygame.image.load("images/death.png").convert_alpha()
end = pygame.transform.scale(end, (1200, 800))
#arrow = pygame.transform.scale(arrow, (75, 75))
player = player.get_rect(center=((window_width/2), (window_height/2)))

    
#fade in and out when changing cells
def cell_change_anim(x_pos, y_pos, c1, c2):
    fadeIn = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill(Colours.BLACK)
    for i in range(0, 260, 5):
        #win.fill((c1.colour))
        c1.blits(c1)
        #win.blits(((c1.imgs[0], c1.rects[0]), (c1.imgs[1], c1.rects[1]), (arrow, player),
        win.blit(fadeIn, (0, 0))
        fadeIn.set_alpha(i)
        pygame.display.update()
        pygame.time.wait(5)
    player.x = x_pos
    player.y = y_pos

    fadeOut = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeOut.fill(Colours.BLACK)
    alpha = 255
    while alpha > 0:
        #win.fill((c2.colour))
        c2.blits(c2)
        #win.blits(((c2.imgs[0], c2.rects[0]), (c2.imgs[1], c2.rects[1]), (arrow, player),
        win.blit(fadeOut, (0, 0))
        fadeOut.set_alpha(alpha)
        pygame.display.update()
        pygame.time.wait(5)
        alpha -= 5



class Map:
    #these variables get changed when cells are entered
    wall_1_rect = wall_1.get_rect(center=(1100, 160))
    wall_2 = pygame.transform.scale(midright, (184, 376))
    wall_2_rect = wall_2.get_rect(center=(1112, 508))
    wall_3 = pygame.transform.scale(botright, (640, 232))
    wall_3_rect = wall_3.get_rect(center=(1200, 800))
    img_1 = pygame.transform.scale(rock, (200, 100))
    img_2 = pygame.transform.scale(rock, (500, 100))
    img_3 = pygame.transform.scale(fire, (100, 100))
    obstacle_1 = img_1.get_rect(center=(300, 300))
    obstacle_2 = img_2.get_rect(center=(700, 700))
    obstacle_3 = img_3.get_rect(center=(1000, 400))
    bg = pygame.transform.scale(floor1, (1200, 800))
    stage = "main"
    running = True
    obstacles = [obstacle_1, obstacle_2, obstacle_3, wall_1_rect, wall_2_rect]
    imgs = [img_1, img_2, img_3, wall_1, wall_2]
    combat_1 = False
    facing = "down"
                
    def __init__(self):
        #starts game
        if self.running == True:
            Map.game(Map.bg, Map.stage, Map.running)
            
    def combat_placeholder():
        #can call combat function here, makes it not repeat upon re-entering room
        if Map.combat_1 == False:
            result = battle("Mole Rat", 100, 50, playerStr, playerHP, playerSpeed, 10)
            print(stats.playerHP)
            while stats.playerHP <= 0:
                win.blit(end, (0, 0))
                pygame.display.update()
            pygame.time.wait(100000)

            Map.combat_1 = True
            
    def game(bg, cell, run):
        #called by init to start game
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
            #gets player positions as variables
            player_x = player.x
            player_y = player.y
            speed = 5
            
            #sets fps
            clock.tick(60)
            #gets key presses
            keys = pygame.key.get_pressed()

            #if w pressed, move player up
            if keys[pygame.K_w] and player.top > 0:
                player.y -= speed
                Map.facing = "up"
                #if player hits a rect, move them back equal to their speed
                #(they don't move at all)
                if player.collideobjects(Map.obstacles):
                    player.y += speed
            #if s pressed, move down
            elif keys[pygame.K_s] and player.bottom < window_height:
                player.y += speed
                Map.facing = "down"
                if player.collideobjects(Map.obstacles):
                    player.y -= speed
            #if a pressed, move left
            elif keys[pygame.K_a] and player.left > 0:
                player.x -= speed
                Map.facing = "left"
                if player.collideobjects(Map.obstacles):
                    player.x += speed
            #if d pressed, move right
            elif keys[pygame.K_d] and player.right < window_width:
                player.x += speed
                Map.facing = "right"
                if player.collideobjects(Map.obstacles):
                    player.x -= speed
            

            #displays sprites for each individual cell,
            #and when player hits a border, changes the cell
            if cell == "main":
                cell_1.blits(cell_1) #displays sprites
                if player.top <= 0:
                    #calls the fade animation
                    cell_change_anim(player_x, (window_height - 101), cell_1, cell_2)
                    #calls cell_2 function
                    cell_2()
                '''elif player.bottom >= window_height:
                    cell_change_anim(player_x, 1, cell_1, cell_3)
                    cell_3()
                elif player.right >= window_width:
                    cell_change_anim(1, player_y, cell_1, cell_4)
                    cell_4()
                elif player.left <= 0:
                    cell_change_anim((window_width - 101), player_y, cell_1, cell_6)
                    cell_6()'''
                    
            #when player is in cell_2 (go up from main cell), displays sprites from cell_2
            elif cell == "up":
                cell_2.blits(cell_2)
                if player.bottom >= window_height:
                    cell_change_anim(player_x, 1, cell_2, cell_1)
                    cell_1()

            #cell_3 stuff (down from main)
            elif cell == "down":
                if player.top <= 0:
                    cell_change_anim(player_x, (window_height - 101), cell_3, cell_1)
                    cell_1()
                    
            #cell_6 stuff (left from main)
            elif cell == "left":
                if player.right >= window_width:
                    cell_change_anim(1, player_y, cell_6, cell_1)
                    cell_1()

            #cell_4 stuff (right from main)
            elif cell == "right":
                if player.left <= 0:
                    cell_change_anim((window_width - 101), player_y, cell_4, cell_1)
                    cell_1()

            pygame.display.update()
                

        pygame.quit()


class cell_1(Map):
    #cell_1 variables
    wall_1 = pygame.transform.scale(right, (127, 800))
    wall_1_rect = wall_1.get_rect(center=(1136, 400))
    wall_2 = pygame.transform.scale(midright, (138, 282))
    wall_2_rect = wall_2.get_rect(center=(600, 400))
    wall_3 = pygame.transform.scale(botright, (480, 225))
    wall_3_rect = wall_3.get_rect(center=(962, 713))
    img_1 = pygame.transform.scale(rock, (200, 100))
    img_2 = pygame.transform.scale(rock, (500, 100))
    img_3 = pygame.transform.scale(fire, (100, 100))
    obstacle_1 = img_1.get_rect(center=(300, 300))
    obstacle_2 = img_2.get_rect(center=(700, 700))
    obstacle_3 = img_3.get_rect(center=(1000, 400))
    bg = pygame.transform.scale(floor1, (window_width, window_height))
    stage = "main"
    rects = [obstacle_1, obstacle_2, obstacle_3, wall_1_rect, wall_2_rect,
             wall_3_rect]
    imgs = [img_1, img_2, img_3, wall_1, wall_2, wall_3]
    def __init__(self):
        #Map.colour = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
        
    def blits(self):
        win.blits(((self.bg, (0, 0)), (self.imgs[3], self.rects[3]),
                   (self.imgs[5], self.rects[5]),
                   (self.imgs[4], self.rects[4]), (self.imgs[0], self.rects[0]),
                   (self.imgs[1], self.rects[1]),(self.imgs[2], self.rects[2])
                   ))

        if Map.facing == "up":
            win.blit(back, player)
        else:
            win.blit(arrow, player)


class cell_2(Map):
    img_1 = pygame.transform.scale(rock, (100, 100))
    img_2 = pygame.transform.scale(rock, (300, 100))
    obstacle_1 = img_1.get_rect(center=(100, 100))
    obstacle_2 = img_2.get_rect(center=(500, 500))
    #colour = "pink"
    colour = pygame.transform.scale(cave2, (window_width, window_height))
    stage = "up"
    rects = [obstacle_1, obstacle_2]
    rects = []

    imgs = [img_1, img_2]
    def __init__(self):
        Map.combat_placeholder()
        Map.colour = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
        
    def blits(self):
        #win.blits(((self.colour, (0, 0)), (self.imgs[0], self.rects[0]), (self.imgs[1], self.rects[1])))
        win.blit(self.colour, (0, 0))

        if Map.facing == "up":
            win.blit(back, player)
        else:
            win.blit(arrow, player)

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
