#Libraries and other file imports
import random
import pygame
pygame.init()
pygame.font.init()
from healthbar import *
from Textrender import *
import stats
from game import *
from audio import * 

clock = pygame.time.Clock()
window_height = 800
window_width = 1200

#Config of images sounds and font
#TODO Put any new sounds here.
font = pygame.font.Font('PanicStricken.ttf', 40)
combat = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The Discovery Of Fear: Ooga Booga Beatdown - Combat")
image1 = pygame.image.load("images/button.png").convert_alpha()
textboximage = pygame.image.load("images/TextBox.png").convert_alpha()
buttonaudio = pygame.mixer.Sound(sound_collection[0])
combatmusic = music_collection[2]
punch = pygame.mixer.Sound(sound_collection[2])

#The molerat
molerat = pygame.image.load("images/molerat.png").convert_alpha()
dead_molerat = pygame.image.load("images/dead_molerat.png").convert_alpha()
molerat = pygame.transform.scale(molerat, (1200, 800))
dead_molerat = pygame.transform.scale(dead_molerat, (1200,800))
slime = pygame.image.load("images/slimecombat.png").convert_alpha()
slime = pygame.transform.scale(slime, (window_width, window_height))

#Text 
attack_text = font.render("Attack", True, "red")
flee_text = font.render("Flee", True, "red")
victory_text = font.render("You won!", True, "green")

#The buttons
image2 = pygame.transform.scale(image1, (150, 60))
image1 = pygame.transform.scale(image1, (150, 60))
textboximage2 = pygame.transform.scale(textboximage, (480, 80))
textboximage = pygame.transform.scale(textboximage, (340, 50))

#Default combat message in case of error
combat_message = font.render("Error", True, "red")
strength = font.render(f"Your strength: {Stats.playerStr}", True, "red")
run = font.render(f"You sucesfully fled battle.", True, "yellow")


button = image1.get_rect()
button2 = image2.get_rect()
textbox = textboximage.get_rect()

button.center = (900, 700)
button2.center = (1100, 700)
textbox.center = (550, 450)

def moleratblits():
    combat.blits(((molerat, (0, 0)), (image1, (button.x, button.y)), (image2, (button2.x, button2.y)), (attack_text, (button.x +10, button.y + 5)), (flee_text, (button2.x +10, button2.y +5)), (textboximage, (830,750)), (strength, (850, 750))))

def slimeblits():
    combat.blits(((slime, (0, 0)), (image1, (button.x, button.y)), (image2, (button2.x, button2.y)), (attack_text, (button.x +10, button.y + 5)), (flee_text, (button2.x +10, button2.y +5)), (textboximage, (830,750)), (strength, (850, 750))))

def victory_blits():
    combat.blits(((dead_molerat, (0,0)), (victory_text, (600,400))))
    pygame.display.update()
    pygame.time.wait(2000)

def flee_blits():
    combat.blits(((textboximage2, (480, 290)), (run, (500,300))))
    pygame.display.update()
    pygame.time.wait(2000)


#Function for the battle. Takes 5 parameters (1 string 4 ints) and will take the player stats from Stats.py once that works.
def battle(enemyType, enemyStr, enemyHP, playerStr, playerHP, playerSpeed, enemySpeed):

    #combat_message displayed once at beginning of battle
    combat_message = f"A {enemyType} attacks you! |Strength: {enemyStr} HP: {enemyHP}"

    music(combatmusic)
    pygame.mixer.music.set_volume(0.6)
    #this loop keeps going until the end of the battle
    fighting = True
    while fighting:
        #for loop so the close button works: DO NOT MODIFY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fighting = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    sound(buttonaudio)
                    pygame.time.wait(150)
                    #checks to see if player is faster then enemy
                    if playerSpeed >= enemySpeed:
                        enemyHP -= playerStr
                        sound(punch)
                        if enemyHP <= 0:
                            fighting = False
                        playerHP -= enemyStr
                        if playerHP <= 0:
                            pygame.mixer.music.fadeout(1000)
                            print("died")
                            Stats.playerHP = playerHP
                            return "player loss"
                        combat_message = f'You attacked the {enemyType}, dealing {playerStr} damage! |The {enemyType} attacks you, dealing {enemyStr} damage. |Enemy HP: {enemyHP}'
                    #same code except if the enemy is faster
                    else:
                        Stats.playerHP -= enemyStr
                        if Stats.playerHP <= 0:
                            pygame.mixer.music.fadeout(1000)
                            return "player loss"
                        enemyHP -= Stats.playerStr
                        if enemyHP <= 0:
                            fighting = False
                        combat_message = f'The {enemyType} attacks you, dealing {enemyStr} damage. |You attacked the {enemyType}, dealing {playerStr} damage! |Enemy HP: {enemyHP}'

                elif button2.collidepoint(event.pos):
                    sound(buttonaudio)
                    pygame.time.wait(400)
                    run = random.randint(0, 2)
                    #if sucessful, ends battle
                    if run <= 1:
                        flee_blits()
                        Stats.playerHP = playerHP
                        pygame.mixer.music.fadeout(1000)
                        return "You ran away!"
                    #if unsucessful, enemy attacks as normal and your turn is skipped.
                    else:
                        playerHP -= enemyStr
                        if playerHP <= 0:
                            pygame.mixer.music.fadeout(1000)
                            return "player loss"
                        #new combat_message describing failed escape. Sucess does not need a combat_message as loop is exited.
                        combat_message = f"You could not get away. The {enemyType} attacked you. |Enemy HP: {enemyHP}"

        clock.tick(60)
        combat.fill((69, 69, 69))

        health_bar.hp = playerHP

        a, b = pygame.mouse.get_pos()
        if button.x <= a <= button.x + 100 and button.y <= b <= button.y +60:
            image1.set_alpha(210)
            attack_text.set_alpha(210)
        else:
            image1.set_alpha(255)
            attack_text.set_alpha(255)
        if button2.x <= a <= button2.x + 110 and button2.y <= b <= button2.y +60:
            image2.set_alpha(210)
            flee_text.set_alpha(210)
        else:
            image2.set_alpha(255)
            flee_text.set_alpha(255)
        
        if enemyHP > 0:
            if enemyType == "Mole Rat":
                moleratblits()
            elif enemyType == "Slime":
                slimeblits()
            blit_text(combat, combat_message, (100, 100), font, "red")
            health_bar.draw(combat)
            combat.blit(heart,(950,5))

        else:
            victory_blits()
            fighting = False
        pygame.display.flip()

        pygame.display.update()

    #Default return. If the loop is exited without any return value.
    Stats.playerHP = playerHP
    pygame.mixer.music.fadeout(1000)
    return "enemy vanquished"
    
