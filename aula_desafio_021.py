# reproduzir um audio de um arquivo MP3
import playsound
playsound.playsound('bob.mp3')
playsound.playsound('errolgarner.mp3')


# reproduzir um audio de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('errolgarner.mp3')
pygame.mixer.music.play()
pygame.event.wait()
