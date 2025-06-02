import pygame

#Starting stats
class Stats:
    basePlayerHP = 100
    baseStr = 10
    playerStr = 10
    maxPHP = 100
    playerHP = 100
    playerSpeed = 10

def gainHealth(gain):
    Stats.playerHP += gain
    Stats.maxPHP += gain

def gainSpeed(gain):
    Stats.playerSpeed += gain

def gainStrength(gain):
    Stats.playerStr += gain

def Heal(rate):
    if Stats.playerHP < Stats.maxPHP:
        Stats.playerHP += 10
        print(Stats.playerHP)
        pygame.time.wait(rate)

