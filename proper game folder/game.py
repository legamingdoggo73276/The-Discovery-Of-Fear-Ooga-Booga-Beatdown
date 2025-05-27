import pygame
from fight import battle
import stats
from healthbar import *
from audio import *

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
pygame.display.set_caption("The Discovery Of Fear: Ooga Booga Beatdown")
clock = pygame.time.Clock()

#loading images and creating player
cave1 = pygame.image.load("images/cavemain.png").convert_alpha()
mole = pygame.image.load("images/mole.png").convert_alpha()
cave2 = pygame.image.load("images/cave2.png").convert_alpha()
cave3 = pygame.image.load("images/cave3.png").convert_alpha()
front = pygame.image.load("images/caveman.png").convert_alpha()
back = pygame.image.load("images/back.png").convert_alpha()
right = pygame.image.load('images/right.png').convert_alpha()
left = pygame.image.load("images/left.png").convert_alpha()
fire = pygame.image.load("images/fire.png").convert_alpha()
rock = pygame.image.load("images/rock.png").convert_alpha()
end = pygame.image.load("images/death.png").convert_alpha()
end = pygame.transform.scale(end, (1200, 800))
player = front.get_rect(center=((window_width/2), (window_height/2)))

#needed audios
current_music = None
fire_audio = pygame.mixer.Sound(sound_collection[4])
cave = music_collection[1]
encounter = pygame.mixer.Sound(sound_collection[1])
    
#fade in and out when changing cells
def cell_change_anim(x_pos, y_pos, c1, c2):
    fadeIn = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeIn.set_alpha(0)
    fadeIn.fill(Colours.BLACK)
    for i in range(0, 260, 5):
        c1.blits(c1)
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
        c2.blits(c2)
        win.blit(fadeOut, (0, 0))
        fadeOut.set_alpha(alpha)
        pygame.display.update()
        pygame.time.wait(5)
        alpha -= 5



class Map:
    #these variables get changed when cells are entered
    #they start as the same ones that are in cell_1
    rect1 = pygame.Rect(620, 625, 580, 175)
    rect2 = pygame.Rect(1095, 0, 105, 800)
    rect3 = pygame.Rect(700, 0, 555, 200)
    rect4 = pygame.Rect(0, 0, 510, 180)
    rect5 = pygame.Rect(0, 0, 135, 800)
    rect6 = pygame.Rect(0, 625, 500, 175)
    img_1 = pygame.transform.scale(rock, (200, 100))
    img_2 = pygame.transform.scale(rock, (500, 100))
    img_3 = pygame.transform.scale(fire, (100, 100))
    moleimg = pygame.transform.scale(mole, (50, 50))
    obstacle_1 = img_1.get_rect(center=(300, 300))
    obstacle_2 = img_2.get_rect(center=(700, 700))
    obstacle_3 = img_3.get_rect(center=(1000, 400))
    music = cave
    sound = fire_audio
    
    bg = pygame.transform.scale(cave1, (1200, 800))
    stage = "main"
    running = True
    obstacles = [rect1, rect2, rect3, rect4, rect5, rect6, obstacle_3]
    imgs = [img_1, img_2, img_3]
    combat_1 = False
    facing = "down"
                
    def __init__(self):
        #starts game
        if self.running == True:
            Map.game(Map.bg, Map.stage, Map.running)
            
    def combat_placeholder():
        #can call combat function here, makes it not repeat upon re-entering room
        if Map.combat_1 == False:
            win.blit(Map.moleimg, (550, 350))
            pygame.display.update()
            pygame.time.wait(2000)
            #makes the mole grow and start combat
            for size in range(50, 2000, 50):
                win.blits(((cell_2.colour, (0,0)), (Map.moleimg, ((600-size/2), (400-size/1.75)))))
                Map.moleimg = pygame.transform.scale(Map.moleimg, (size, size))                
                pygame.display.update()
                pygame.time.wait(10)
                
            result = battle("Mole Rat", 10, 50, playerStr, playerHP, playerSpeed, 10)
            print(stats.playerHP)
            while stats.playerHP <= 0:
                win.blit(end, (0, 0))
                pygame.display.update()
                pygame.time.wait(5000)
                pygame.quit()

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
            speed = 20
            
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
                    cell_3()'''
                
                    
            #when player is in cell_2 (go up from main cell), displays sprites from cell_2
            elif cell == "up":
                cell_2.blits(cell_2)
                if player.bottom >= window_height:
                    cell_change_anim(player_x, 1, cell_2, cell_1)
                    cell_1()
                elif player.top <= 0:
                    cell_change_anim(player_x, (window_height - 101), cell_2, cell_3)
                    cell_3()

            #cell_3 stuff (down from main)
            elif cell == "up2":
                cell_3.blits(cell_3)
                if player.bottom >= window_height:
                    cell_change_anim(player_x, 1, cell_3, cell_2)
                    cell_2()
                    
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
    rect1 = pygame.Rect(620, 625, 580, 175)
    rect2 = pygame.Rect(1095, 0, 105, 800)
    rect3 = pygame.Rect(700, 0, 555, 200)
    rect4 = pygame.Rect(0, 0, 510, 180)
    rect5 = pygame.Rect(0, 0, 135, 800)
    rect6 = pygame.Rect(0, 625, 500, 175)
    img_1 = pygame.transform.scale(rock, (200, 100))
    img_2 = pygame.transform.scale(rock, (500, 100))
    img_3 = pygame.transform.scale(fire, (100, 100))
    obstacle_1 = img_1.get_rect(center=(300, 300))
    obstacle_2 = img_2.get_rect(center=(700, 700))
    obstacle_3 = img_3.get_rect(center=(1000, 400))
    music = cave
    sound = fire_audio
    bg = pygame.transform.scale(cave1, (window_width, window_height))
    stage = "main"
    rects = [rect1, rect2, rect3, rect4, rect5, rect6, obstacle_3]
    imgs = [img_1, img_2, img_3]
    def __init__(self):
        
        #fire_audio.play(-1)
        Map.music = self.music 
        Map.sound = self.sound
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
        
    def blits(self):
        #blits all the sprites for this room on the screen
        #the line under this is the background and the campfire
        win.blits(((self.bg, (0,0)), (self.imgs[2], self.rects[6])))

        #blits a different version of the caveman depending on which way you're facing
        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)


class cell_2(Map):
    rect1 = pygame.Rect(0, 0, 510, 800)
    rect2 = pygame.Rect(680, 0, 510, 800)
    img_1 = pygame.transform.scale(rock, (100, 100))
    img_2 = pygame.transform.scale(rock, (300, 100))
    obstacle_1 = img_1.get_rect(center=(100, 100))
    obstacle_2 = img_2.get_rect(center=(500, 500))
    colour = pygame.transform.scale(cave2, (window_width, window_height))
    stage = "up"
    rects = [rect1, rect2]
    imgs = [img_1, img_2]
    
    def __init__(self):
        #Map.combat_placeholder()
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
        
    def blits(self):
        #blits all the sprites on the screen
        win.blit(self.colour, (0, 0)) #this one is the background

        if Map.combat_1 == False: #mole sprite, only if it hasnt been beaten
            win.blit(Map.moleimg, (550, 350))
            
        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)

class cell_3(Map):
    rect1 = pygame.Rect(0, 0, 430, 800)
    rect2 = pygame.Rect(680, 0, 510, 800)
    colour = pygame.transform.scale(cave3, (window_width, window_height))
    stage = "up2"
    rects = [rect1, rect2]

    def __init__(self):
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map()
        
    def blits(self):
        win.blit(self.colour, (0, 0))
        pygame.draw.rect(win, 'white', self.rect1)
        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)
            
class cell_4(Map):
    colour = "orange"
    stage = "right"
    def __init__(self):
        Map.bg = self.colour
        Map.stage = self.stage
        Map()
class cell_5(Map):
    colour = "orange"
    stage = "up-right"
    def __init__(self):
        Map.bg = self.colour
        Map.stage = self.stage
        Map()
class cell_6(Map):
    colour = "purple"
    stage = "left"
    def __init__(self):
        Map.bg = self.colour
        Map.stage = self.stage
        Map()
    
        
#Map()
