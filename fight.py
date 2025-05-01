import random

#Function for the battle. Takes 5 parameters (1 string 4 ints) and will take the player stats from Stats.py once that works.
def battle(enemyType, enemyStr, enemyHP, playerStr, playerHP):

    #Message displayed once at beginning of battle
    message = "An", enemyType, "attacks you! \nStrength:", enemyStr, "\nHP:", enemyHP, "\n \nYour strength:", playerStr, "\nYour HP:", playerHP

    #this loop keeps going until the end of the battle
    fighting = True
    while fighting:
        #prints the current message
        print (message)
        #user input for their action
        action = int(input("0 to attack, 1 to open bag, 2 to run "))

        #if the user chooses to attack
        if action == 0:
            enemyHP -= playerStr
            if enemyHP <= 0:
                fighting = False
            playerHP -= enemyStr
            if playerHP <= 0:
                return "player loss"
            
            #new message describing the attack
            message = "You attacked the", enemyType, "! \n Enemy HP:", enemyHP, "\nPlayer HP:", playerHP
        
        #This is a placeholder until we code inventory.
        elif action == 1:
            print("Bag opened")

        #If the user chooses to run away. 66% chance of sucess.
        elif action == 2:
            run = random.randint(0, 2)
            #if sucessful, ends battle
            if run <= 1:
                print("You ran away!")
                return "player flees"
            #if unsucessful, enemy attacks as normal and your turn is skipped.
            else:
                playerHP -= enemyStr
                if playerHP <= 0:
                    return "player loss"
                #new message describing failed escape. Sucess does not need a message as loop is exited.
                message = "You could not get away. The ghoul attacked you.\nEnemy HP:", enemyHP, "\nPlayer HP:", playerHP

        #This will be removed eventually. It is to find errors.
        else:
            print("force quit")
            fighting = False

    #Default return. If the loop is exited without any return value.
    return "enemy vanquished"


print(battle("ghoul", 5, 50, 10, 100))