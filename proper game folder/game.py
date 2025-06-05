import pygame
import fight
import stats
from healthbar import *
from audio import *
from outro import play_outro

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
cave0 = pygame.image.load("images/startingroom.png").convert_alpha()
cave1 = pygame.image.load("images/cavemain.png").convert_alpha()
mole = pygame.image.load("images/mole.png").convert_alpha()
bat = pygame.image.load("images/bat.png").convert_alpha()
alienguy = pygame.image.load("images/aliensprite.png").convert_alpha()
slimefight = pygame.image.load("images/slimecombat.png").convert_alpha()
slime1 = pygame.image.load("images/babyslime.png").convert_alpha()
slime2 = pygame.image.load("images/slimedown.png").convert_alpha()
slime3 = pygame.image.load("images/bigslime.png").convert_alpha()
cave2 = pygame.image.load("images/cave2.png").convert_alpha()
cave3 = pygame.image.load("images/cave3.png").convert_alpha()
cave4 = pygame.image.load("images/slimeroom.png").convert_alpha()
caveend = pygame.image.load("images/CaveExit.png").convert_alpha()
alienroom = pygame.image.load("images/alien.png").convert_alpha()
void = pygame.image.load("images/wellesley_station.png").convert_alpha()
bend = pygame.image.load("images/bend.png").convert_alpha()
treasureroom = pygame.image.load("images/treasure.png").convert_alpha()
spear = pygame.image.load("images/spear.png").convert_alpha()
front = pygame.image.load("images/caveman.png").convert_alpha()
back = pygame.image.load("images/back.png").convert_alpha()
right = pygame.image.load('images/right.png').convert_alpha()
left = pygame.image.load("images/left.png").convert_alpha()
fire = pygame.image.load("images/fire.png").convert_alpha()
rock = pygame.image.load("images/rock.png").convert_alpha()
end = pygame.image.load("images/death.png").convert_alpha()
textboximage = pygame.image.load("images/TextBox.png").convert_alpha()
font = pygame.font.Font('PanicStricken.ttf', 40)
encounter = pygame.mixer.Sound(sound_collection[1])
end = pygame.transform.scale(end, (1200, 800))
player = front.get_rect(center=((window_width/2), (window_height/2)))

#audios
current_music = None 
cave = music_collection[1]
fire_audio = pygame.mixer.Sound(sound_collection[3])
bridge_audio = music_collection[3]
void_audio = music_collection[4]
outro_played = False

    
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

def ending_fade():
    fadeOut = pygame.Surface((window_width, window_height)).convert_alpha()
    fadeOut.fill((0, 0, 0))
    for alpha in range(0, 256, 10):
        fadeOut.set_alpha(alpha)
        win.blit(fadeOut, (0, 0))
        pygame.display.update()
        pygame.time.wait(20)



class Map:
    #they start as the same ones that are in cell_1
    rect1 = pygame.Rect(0, 710, 1200, 90)
    rect2 = pygame.Rect(925, 0, 275, 800)
    rect3 = pygame.Rect(675, 0, 525, 300)
    rect4 = pygame.Rect(0, 0, 510, 275)
    rect5 = pygame.Rect(0, 0, 250, 800)
    moleimg = pygame.transform.scale(mole, (50, 50))
    babyslime = pygame.transform.scale(slime1, (100, 100))
    slimedown = pygame.transform.scale(slime2, (100, 100))
    bigslime = pygame.transform.scale(slime3, (150, 150))
    batimg = pygame.transform.scale(bat, (50, 50))
    slime = babyslime
    
    #these variables get changed when cells are entered
    bg = pygame.transform.scale(cave0, (1200, 800))
    stage = "start"
    running = True
    obstacles = [rect1, rect2, rect3, rect4, rect5]
    imgs = []
    combat_1 = False
    combat_2 = False
    combat_3 = False
    combat_4 = False
    spear_obtain = False
    facing = "down"
    obtain_message = "Error"
                
    def __init__(self):
        #starts game
        global current_music
        if current_music != cave:
            music(cave)
            current_music = cave
        if self.running == True:
            Map.game(Map.bg, Map.stage, Map.running)

    def mole_combat():
        #can call combat function here, makes it not repeat upon re-entering room
        if Map.combat_1 == False:
            win.blit(Map.moleimg, (550, 350))
            pygame.display.update()
            pygame.time.wait(2000)
            sound(encounter)
            #makes the mole grow and start combat
            for size in range(50, 2000, 50):
                win.blits(((cell_2.colour, (0,0)), (back, player), (Map.moleimg, ((600-size/2), (400-(size/1.9))))))
                Map.moleimg = pygame.transform.scale(Map.moleimg, (size, size))
                pygame.display.update()
                pygame.time.wait(10)
                
            result = fight.battle("Mole Rat", 10, 50, Stats.playerStr, Stats.playerHP, Stats.playerSpeed, 10)
            print(Stats.playerHP)
            while Stats.playerHP <= 0:
                win.blit(end, (0, 0))
                pygame.display.update()
                pygame.time.wait(5000)
                pygame.quit()

            global current_music
            music(cave)
            current_music = cave

            Map.combat_1 = True
    def slime_combat():
        #can call combat function here, makes it not repeat upon re-entering room
        if Map.combat_2 == False:
            win.blit(Map.babyslime, (550, 350))
            pygame.display.update()
            pygame.time.wait(1000)
            Map.slime = Map.slimedown
            cell_3.blits(cell_3)
            pygame.display.update()
            pygame.time.wait(500)
            Map.slime = Map.bigslime
            cell_3.blits(cell_3)
            pygame.display.update()
            pygame.time.wait(1000)
            sound(encounter)
            for size in range(150, 2000, 75):
                win.blits(((cell_3.colour, (0, 0)), (back, player), (Map.bigslime, ((600-size/2), (400-size/1.75)))))
                Map.bigslime = pygame.transform.scale(Map.bigslime, (size, size))
                pygame.display.update()
                pygame.time.wait(20)

            result = fight.battle("Slime", 10, 50, Stats.playerStr, Stats.playerHP, Stats.playerSpeed, 10)
            print(Stats.playerHP)
            while Stats.playerHP <= 0:
                win.blit(end, (0, 0))
                pygame.display.update()
                pygame.time.wait(5000)
                pygame.quit()

            global current_music
            music(bridge_audio)
            current_music = bridge_audio

            Map.combat_2 = True

    def bat_combat():
        #can call combat function here, makes it not repeat upon re-entering room
        if Map.combat_3 == False:
            win.blit(Map.batimg, (550, 350))
            pygame.display.update()
            pygame.time.wait(1000)
            sound(encounter)
            for size in range(50, 2000, 50):
                win.blits(((cell_8.colour, (0,0)), (Map.batimg, ((600-size/2), (400-size/1.75)))))
                Map.batimg = pygame.transform.scale(Map.batimg, (size, size))                
                pygame.display.update()
                pygame.time.wait(10)

            result = fight.battle("Bat", 10, 50, Stats.playerStr, Stats.playerHP, Stats.playerSpeed, 10)
            print(Stats.playerHP)
            while Stats.playerHP <= 0:
                win.blit(end, (0, 0))
                pygame.display.update()
                pygame.time.wait(5000)
                pygame.quit()

            global current_music
            music(cave)
            current_music = cave

            Map.combat_3 = True
        
    def alien_combat():
        if not Map.combat_4:
            win.blit(Map.alienguy, (950, 350))
            pygame.display.update()
            pygame.time.wait(2000)
            sound(encounter)
            for size in range(50, 2000, 50):
                win.blits(((cell_6.colour, (0, 0)), (right, player), (Map.alienguy, ((950-size/1.3), (400-size/1.75)))))
                Map.alienguy = pygame.transform.scale(Map.alienguy, (size, size))
                pygame.display.update()
                pygame.time.wait(10)
                
            result = fight.battle("Alien", 10, 50, Stats.playerStr, Stats.playerHP, Stats.playerSpeed, 10)
            Map.combat_4 = True
            
    def item_obtain(item):
        if item == "spear":
            gainStrength(5)
        #elif item == "raygun":
            #gainStrength(10)
        Map.obtain_message = font.render(f"You have obtained the {item}!", True, "red")
        textboximg = pygame.transform.scale(textboximage, (600, 50))
        #textboxrect = textboximage.get_rect()
        win.blits(((textboximg, (450, 500)), (Map.obtain_message, (500, 500))))
        win.blit(Map.obtain_message, (500, 500))
        pygame.display.update()
        pygame.time.wait(2000)
    
    def healthbarprint():
        health_bar.hp = Stats.playerHP
        health_bar.draw(win)
        win.blit(heart,(950,5))


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
            if cell == "start":
                starting_cell.blits(starting_cell)
                if player.top <= 0:
                    #calls the fade animation
                    cell_change_anim(550, (window_height - 101), starting_cell, cell_1)
                    #calls cell_1 function
                    cell_1()

            elif cell == "main":
                cell_1.blits(cell_1) #displays sprites
                if cell_1.obstacle_3.left - player.right < speed and cell_1.obstacle_3.left - player.right > -130 and keys[pygame.K_e]:
                    if cell_1.obstacle_3.top - player.bottom < speed and cell_1.obstacle_3.bottom - player.top > -10:
                        Heal(100)
                        print(Stats.playerHP)
                        #for interacting with campfire
                if player.top <= 0:
                    #calls the fade animation
                    cell_change_anim(550, (window_height - 101), cell_1, cell_2)
                    #calls cell_2 function
                    cell_2()
                elif player.bottom >= window_height:
                    cell_change_anim(550, 1, cell_1, starting_cell)
                    starting_cell()
            
            #when player is in cell_2 (go up from main cell), displays sprites from cell_2
            elif cell == "up":
                cell_2.blits(cell_2)
                if player.bottom >= window_height:
                    cell_change_anim(550, 1, cell_2, cell_1)
                    cell_1()
                elif player.top <= 0:
                    cell_change_anim(550, (window_height - 101), cell_2, cell_4)
                    cell_4()

            #cell_3 stuff (up twice from main)
            elif cell == "up2":
                cell_3.blits(cell_3)
                if player.bottom >= window_height:
                    cell_change_anim(1000, 1, cell_3, cell_4)
                    cell_4()
                if player.top <= 0:
                    cell_change_anim(550, (window_height - 101), cell_3, cell_5)
                    cell_5()

            elif cell == "slime":
                cell_4.blits(cell_4)
                if player.top <= 0:
                    cell_change_anim(550, (window_height - 101), cell_4, cell_3)
                    cell_3()
                elif player.bottom >= window_height:
                    cell_change_anim(550, 1, cell_4, cell_2)
                    cell_2()
                elif player.left <= 0:
                    cell_change_anim((window_width - 101), 359, cell_4, cell_7)
                    cell_7()
            #cell_4 stuff (slime)

            elif cell == "treasure":
                cell_7.blits(cell_7)
                if player.colliderect(cell_7.spearrect) and not Map.spear_obtain:
                    Map.spear_obtain = True
                    Map.item_obtain("spear")
                    print(Stats.playerStr)
                if player.right >= window_width:
                    cell_change_anim(1, 280, cell_7, cell_4)
                    cell_4()

            elif cell == "alien":
                cell_5.blits(cell_5)
                if player.bottom >= window_height:
                    cell_change_anim(550, 1, cell_5, cell_3)
                    cell_3()
                elif player.right >= window_width:
                    cell_change_anim(1, 425, cell_5, cell_6)
                    cell_6()
            
            elif cell == "curve":
                cell_6.blits(cell_6)
                if player.left <= 0:
                    cell_change_anim((window_width - 101), 280, cell_6, cell_5)
                    cell_5()
                elif player.top <= 0:
                    cell_change_anim(550, (window_height - 101), cell_6, cell_8)
                    cell_8()
                
            elif cell == "exit":
                cell_8.blits(cell_8)
                if player.bottom >= window_height:
                    cell_change_anim(920, 1, cell_8, cell_6)
                    cell_6()
                elif player.top <= 0:
                    cell_change_anim(550, (window_height - 101), cell_8, cell_9)
                    cell = "void"

            elif cell == "right":
                if player.left <= 0:
                    cell_change_anim((window_width - 101), player_y, cell_4, cell_1)
                    cell_1()

            elif cell == "void":
                global outro_played
                if not outro_played:
                    ending_fade()
                    play_outro(win)
                    outro_played = True
                    pygame.quit()
                else:
                    cell_9.blits(cell_9)

            pygame.display.update()

        pygame.quit()

class starting_cell(Map):
    rect1 = pygame.Rect(0, 710, 1200, 90)
    rect2 = pygame.Rect(925, 0, 275, 800)
    rect3 = pygame.Rect(675, 0, 525, 300)
    rect4 = pygame.Rect(0, 0, 510, 275)
    rect5 = pygame.Rect(0, 0, 250, 800)
    stage = "start"
    bg = pygame.transform.scale(cave0, (window_width, window_height))
    rects = [rect1, rect2, rect3, rect4, rect5]
    imgs = []
    def __init__(self):
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
    def blits(self):
        win.blit(self.bg, (0, 0))
        Map.healthbarprint()

        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)

class cell_1(Map):
    #cell_1 variables
    rect1 = pygame.Rect(630, 625, 570, 175)
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
    bg = pygame.transform.scale(cave1, (window_width, window_height))
    stage = "main"
    rects = [rect1, rect2, rect3, rect4, rect5, rect6, obstacle_3]
    imgs = [img_1, img_2, img_3]
    def __init__(self):
        #replaces variables in Map class with ones from this class
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
        
    def blits(self):
        #blits all the sprites for this room on the screen
        #the line under this is the background and the campfire
        win.blits(((self.bg, (0,0)), (self.imgs[2], self.rects[6])))
        Map.healthbarprint()

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
        global current_music
        if current_music != cave:
            music(cave)
            current_music = cave
        Map.mole_combat()
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
        
    def blits(self):
        #blits all the sprites on the screen
        win.blit(self.colour, (0, 0)) #this one is the background
        Map.healthbarprint()

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
    rect1 = pygame.Rect(0, 0, 440, 800)
    rect2 = pygame.Rect(750, 0, 450, 800)
    colour = pygame.transform.scale(cave3, (window_width, window_height))
    stage = "up2"
    rects = [rect1, rect2]

    def __init__(self):
        global current_music
        print("cell_3 init, current_music:", current_music)
        if current_music != bridge_audio:
            print("Setting bridge music")
            music(bridge_audio)
            current_music = bridge_audio
        if not Map.combat_2:
            Map.slime_combat()
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map()
        
    def blits(self):
        win.blit(self.colour, (0, 0))
        Map.healthbarprint()

        if Map.slime != Map.bigslime and Map.combat_2 == False:
            win.blit(Map.slime, (550, 350))
        elif Map.slime == Map.bigslime and Map.combat_2 == False:
                    win.blit(Map.slime, (500, 300))


        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)
            
class cell_4(Map):
    rect1 = pygame.Rect(1150, 0, 50, 400)
    rect2 = pygame.Rect(680, 400, 520, 400)
    rect3 = pygame.Rect(0, 0, 950, 200)
    rect4 = pygame.Rect(0, 400, 470, 400)
    colour = pygame.transform.scale(cave4, (window_width, window_height))
    stage = "slime"
    rects = [rect1, rect2, rect3, rect4]
    def __init__(self):
        #Still playing cave music after, WILL FIX
        global current_music
        if current_music != cave:
            music(cave)
            current_music = cave
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map()
    def blits(self):
        win.blit(self.colour, (0, 0))
        Map.healthbarprint()
        
        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)
            
class cell_5(Map):
    rect1 = pygame.Rect(1115, 0, 85, 250)
    rect2 = pygame.Rect(1115, 400, 85, 400)
    rect3 = pygame.Rect(0, 0, 1200, 100)
    rect4 = pygame.Rect(0, 600, 500, 200)
    rect5 = pygame.Rect(725, 600, 475, 200)
    rect6 = pygame.Rect(0, 0, 80, 800)
    ship = pygame.Rect(200, 110, 300, 200)
    colour = pygame.transform.scale(alienroom, (window_width, window_height))
    stage = "alien"
    rects = [rect1, rect2, rect3, rect4, rect5, rect6, ship]
    def __init__(self):
        global current_music
        if current_music != cave:
            music(cave)
            current_music = cave
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map()
    def blits(self):
        win.blit(self.colour, (0, 0))
        Map.healthbarprint()
        
        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)
            
class cell_6(Map):
    rect1 = pygame.Rect(0, 570, 1200, 230)
    rect2 = pygame.Rect(0, 0, 800, 360)
    rect3 = pygame.Rect(1120, 0, 80, 800)
    rect4 = pygame.Rect(800, 525, 400, 275)
    colour = pygame.transform.scale(bend, (window_width, window_height))
    stage = "curve"
    rects = [rect1, rect2, rect3, rect4]
    def __init__(self):
        global current_music
        if current_music != cave:
            music(cave)
            current_music = cave
        if not Map.combat_4:
            Map.alien_combat()

        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map()
    def blits(self):
        win.blit(self.colour, (0, 0))
        Map.healthbarprint()
        
        if not Map.combat_4:
            win.blit(Map.alienguy, (950, 350))

        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)
            
class cell_7(Map):
    rect1 = pygame.Rect(0, 0, 1200, 120)
    rect2 = pygame.Rect(0, 0, 230, 800)
    rect3 = pygame.Rect(600, 0, 600, 300)
    rect4 = pygame.Rect(630, 475, 570, 325)
    rect5 = pygame.Rect(0, 640, 1200, 160)
    spearimg = pygame.transform.scale(spear, (100, 100))
    spearrect = spearimg.get_rect(center=(400, 400))
    colour = pygame.transform.scale(treasureroom, (window_width, window_height))
    stage = "treasure"
    rects = [rect1, rect2, rect3, rect4, rect5]
    
    def __init__(self):
        global current_music
        if current_music != cave:
            music(cave)
            current_music = cave
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map.imgs = self.imgs
        Map()
        
    def blits(self):
        win.blit(self.colour, (0, 0))
        Map.healthbarprint()
        
        if Map.spear_obtain == False:
            win.blit(self.spearimg, (400, 400))
        
        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)

class cell_8(Map):
    rect1 = pygame.Rect(0, 0, 380, 800)
    rect2 = pygame.Rect(790, 0, 410, 800)
    exitrect = pygame.Rect(380, 0, 410, 200)
    colour = pygame.transform.scale(caveend, (window_width, window_height))
    stage = "exit"
    rects = [rect1, rect2]
    def __init__(self):
        global current_music
        if current_music != cave:
            music(cave)
            current_music = cave
        Map.bat_combat()
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
        Map()
    
    def blits(self):
        win.blit(self.colour, (0, 0))
        Map.healthbarprint()

        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)

class cell_9(Map):
    colour = pygame.transform.scale(void, (window_width, window_height))
    stage = "blank"
    rects = []
    def __init__(self):
        global current_music
        if current_music != void_audio:
            music(void_audio)
            current_music = void_audio
        Map.bg = self.colour
        Map.stage = self.stage
        Map.obstacles = self.rects
    
    def blits(self):
        win.blit(self.colour, (0, 0))
        
        if Map.facing == "up":
            win.blit(back, player)
        elif Map.facing == "right":
            win.blit(right, player)
        elif Map.facing == "left":
            win.blit(left, player)
        else:
            win.blit(front, player)

#Map()
