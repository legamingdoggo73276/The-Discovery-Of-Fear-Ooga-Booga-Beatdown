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

#Config of images sounds and font
#TODO Put any new sounds here.
font = pygame.font.Font('who-asks-satan.ttf', 40)
combat = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The Discovery Of Fear: Ooga Booga Beatdown - Combat")
image1 = pygame.image.load("button.png").convert_alpha()
#buttonaudio = pygame.mixer.Sound(sound_collection[0])

#The molerat
molerat = pygame.image.load("molerat.png").convert_alpha()
molerat = pygame.transform.scale(molerat, (1200, 800))
#audio for combat (work in progress)
#combatmusic = pygame.mixer.music.load
#punch = pygame.mixer.Sound

#Text 
attack_text = font.render("Attack", True, "red")
flee_text = font.render("Flee", True, "red")

#The buttons
image2 = pygame.transform.scale(image1, (150, 60))
image1 = pygame.transform.scale(image1, (150, 60))

#Default combat message in case of error
combat_message = "Error"


button = image1.get_rect()
button2 = image2.get_rect()
button.center = (900, 700)
button2.center = (1100, 700)

def blits():
    combat.blits(((molerat, (0, 0)), (image1, (button.x, button.y)), (image2, (button2.x, button2.y)), (attack_text, (button.x +10, button.y + 5)), (flee_text, (button2.x +10, button2.y +5))))


#Function for the battle. Takes 5 parameters (1 string 4 ints) and will take the player stats from Stats.py once that works.
def battle(enemyType, enemyStr, enemyHP, playerStr, playerHP, playerSpeed, enemySpeed):

    #combat_message displayed once at beginning of battle
    combat_message = f"A {enemyType} attacks you! \nStrength: {enemyStr} \nHP: {enemyHP}\n \nYour strength: {playerStr}"

    #this loop keeps going until the end of the battle
    fighting = True
    while fighting:
        #for loop so the close button works: DO NOT MODIFY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fighting = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    #sound(buttonaudio)
                    pygame.time.wait(400)
                    #checks to see if player is faster then enemy
                    if playerSpeed >= enemySpeed:
                        enemyHP -= playerStr
                        if enemyHP <= 0:
                            fighting = False
                        playerHP -= enemyStr
                        if playerHP <= 0:
                            print("died")
                            stats.playerHP = playerHP
                            return "player loss"
                        combat_message = f'You attacked the {enemyType}, dealing {playerStr} damage! \nThe {enemyType} attacks you, dealing {enemyStr} damage. \nEnemy HP: {enemyHP}'
                    #same code except if the enemy is faster
                    else:
                        playerHP -= enemyStr
                        if playerHP <= 0:
                            return "player loss"
                        enemyHP -= playerStr
                        if enemyHP <= 0:
                            fighting = False
                        combat_message = f'The {enemyType} attacks you, dealing {enemyStr} damage. \nYou attacked the {enemyType}, dealing {playerStr} damage! \nEnemy HP: {enemyHP}'
                elif button2.collidepoint(event.pos):
                    #sound(buttonaudio)
                    pygame.time.wait(400)
                    run = random.randint(0, 2)
                    #if sucessful, ends battle
                    if run <= 1:
                        print("You ran away!")
                        stats.playerHP = playerHP
                        return "You ran away!"
                    #if unsucessful, enemy attacks as normal and your turn is skipped.
                    else:
                        playerHP -= enemyStr
                        if playerHP <= 0:
                            return "player loss"
                        #new combat_message describing failed escape. Sucess does not need a combat_message as loop is exited.
                        combat_message = f"You could not get away. The {enemyType} attacked you.\nEnemy HP: {enemyHP}"

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
        
        blits()       
        combat_message = font.render(combat_message, True, "red")
        combat.blit(combat_message, (800, 600))
        health_bar.draw(combat)
        combat.blit(heart,(950,5))
    
        pygame.display.flip()

        pygame.display.update()

    #Default return. If the loop is exited without any return value.
    stats.playerHP = playerHP
    return "enemy vanquished"
    
