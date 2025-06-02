import pygame

#Starting stats
basePlayerHP = 100
baseStr = 10
playerStr = 10
maxPHP = 100
playerHP = 100
playerSpeed = 10

def gainHealth(gain):
    playerHP += gain
    maxPHP += gain

def gainSpeed(gain):
    playerSpeed += gain

def gainStrength(gain):
    playerStr += gain

def Heal(rate):
    if playerHP <= maxPHP:
        playerHP += 10
        print(playerHP)
        pygame.time.wait(rate)

