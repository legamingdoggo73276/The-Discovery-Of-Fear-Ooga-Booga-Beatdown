import pygame
from stats import *

pygame.init()

#1200 x 800
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Health Bar')
#import heart for healthbar
heart = pygame.image.load("images/heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (250,125))
heart_red = (208,78,90,255)

class HealthBar():
    #for the actual health bar visual
    # # x, y coordinates, width and height (of the health bar rectangle)
    def __init__(self, x, y, w, h, max_hp): 
        self.x = x
        self.y = y 
        self. w = w
        self.h = h
        self.hp = playerHP
        self.max_hp = maxPHP

    def draw(self, surface):
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "black", (self.x, self.y, self.w, self.h))
        #COLOUR: d04f5a
        pygame.draw.rect(surface, heart_red, (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(980, 50, 200, 30, 100)
