import pygame
pygame.init()
from pygame import mixer
mixer.init()

def music(audio):
    #-1 repeats sound forever
    pygame.mixer.Sound.play(audio, -1)

def sound(audio):
    pygame.mixer.Sound.play(audio)

#can keep them as individual variables or just a list and call from list !!
music_collection = ["campfire.mp3", "drip_cave.mp3"]
sound_collection = ["button.mp3", "obtain_item.mp3"]


#background soundtracks
campfire = pygame.mixer.Sound(music_collection[0])
#cave sound is lowkey kinda loud.. fix?
cave = pygame.mixer.Sound(music_collection[1])

#sound effects
button = pygame.mixer.Sound(sound_collection[0])

#repeats background noise until canceled (hopefully)
music(campfire)
music(cave)


sound(button)
