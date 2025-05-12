import pygame
pygame.init()
from pygame import mixer
mixer.init()

def audio(sound):
    pygame.mixer.Sound.play(sound)

#gonna ask Dr. Zarin if this is a reasonable way to access the audio files
button = pygame.mixer.Sound("button_sound.mp3")
audio(button)
