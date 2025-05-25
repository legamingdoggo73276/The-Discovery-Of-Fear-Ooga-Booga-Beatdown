import pygame
pygame.init()
from pygame import mixer
mixer.init()

def music(audio):
    #-1 repeats sound forever
    pygame.mixer.music.play(-1)

def sound(audio):
    pygame.mixer.Sound.play(audio)

#can keep them as individual variables or just a list and call from list !!
music_collection = ["menu.mp3", "cave.mp3", "campfire.mp3"]
sound_collection = ["button.mp3", "encounter.mp3"]


