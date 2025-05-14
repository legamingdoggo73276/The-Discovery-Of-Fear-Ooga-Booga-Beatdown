import pygame
pygame.init()
from pygame import mixer
mixer.init()

def audio(sound):
    pygame.mixer.Sound.play(sound)

#can keep them as indiviual variables or just a list and call from list !!
song_collection = ["button.mp3", "campfire.mp3"]
play_song = pygame.mixer.Sound(song_collection[1])
audio(play_song)
