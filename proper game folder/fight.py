
import random
import pygame
pygame.init()
pygame.font.init()
from healthbar import *
from Textrender import *
import stats

clock = pygame.time.Clock()

font = pygame.font.Font("who-asks-satan.ttf", 40)
combat = pygame.display.set_mode((1200,800))
pygame.display.set_caption("The Discovery Of Fear: Ooga Booga Beatdown - Combat")
molerat = pygame.image.load("images/molerat.png").convert_alpha()
molerat = pygame.transform.scale(molerat, (1200, 800))

combat_message = "Error"

#Function for the battle. Takes 5 parameters (1 string 4 ints) and will take the player stats from Stats.py once that works.
def battle(enemyType, enemyStr, enemyHP, playerStr, playerHP, playerSpeed, enemySpeed):

    #combat_message displayed once at beginning of battle
    combat_message = f"A {enemyType} attacks you! \nStrength: {enemyStr} \nHP: {enemyHP}\n \nYour strength: {playerStr}\nYour HP: {playerHP}"

    #this loop keeps going until the end of the battle
    fighting = True
    while fighting:
        #for loop so the close button works: DO NOT MODIFY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fighting = False
    
        clock.tick(60)
        combat.fill((69, 69, 69))

        health_bar.hp = playerHP
        
        blit_text(combat, combat_message, (600,400), font)
        combat.blit(molerat, (0,0))
        health_bar.draw(combat)
        combat.blit(heart,(950,5))
    
        pygame.display.flip()

        pygame.display.update()

        action = int(input("0 to attack, 1 to open bag, 2 to run "))

        #if the user chooses to attack
        if action == 0:
            #checks to see if player is faster then enemy
            if playerSpeed >= enemySpeed:
                enemyHP -= playerStr
                if enemyHP <= 0:
                    fighting = False
                playerHP -= 100
                if playerHP <= 0:
                    print("died")
                    stats.playerHP = playerHP
                    return "player loss"
                combat_message = f'You attacked the {enemyType}, dealing {playerStr} damage! \nThe {enemyType} attacks you, dealing {enemyStr} damage. \nEnemy HP: {enemyHP} \nPlayer HP:  {playerHP}'
            #same code except if the enemy is faster
            else:
                playerHP -= enemyStr
                if playerHP <= 0:
                    return "player loss"
                enemyHP -= playerStr
                if enemyHP <= 0:
                    fighting = False
                combat_message = f'The {enemyType} attacks you, dealing {enemyStr} damage. \nYou attacked the {enemyType}, dealing {playerStr} damage! \nEnemy HP: {enemyHP} \nPlayer HP:  {playerHP}'
                
        #This is a placeholder until we code inventory.
        elif action == 1:
            print("(Inventory coming soon!)")

        #If the user chooses to run away. 66% chance of sucess.
        elif action == 2:
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
                combat_message = f"You could not get away. The {enemyType} attacked you.\nEnemy HP: {enemyHP} \nPlayer HP: {playerHP}"

        #This will be removed eventually. It is to find errors.
        else:
            print("force quit")
            fighting = False
    #Default return. If the loop is exited without any return value.
    stats.playerHP = playerHP
    return "enemy vanquished"
    
