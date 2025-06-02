import pygame
pygame.init()
pygame.mixer.init()

def music(audio):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(audio)
    #-1 repeats sound forever
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)

def sound(audio):
    pygame.mixer.Sound.play(audio)

#can keep them as individual variables or just a list and call from list !!
music_collection = ["sounds/menu.mp3", "sounds/cave.mp3"]
sound_collection = ["sounds/button.mp3", "sounds/encounter.mp3", "sounds/punch.mp3", "sounds/obtain_item.mp3", "sounds/fire.mp3"]


