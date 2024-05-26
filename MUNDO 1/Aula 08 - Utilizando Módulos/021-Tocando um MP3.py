import pygame
import pygame.key

pygame.mixer.init()
pygame.mixer.music.load('021-senses.mp3')
pygame.mixer.music.play()
input()
pygame.key.stop_text_input('Digite para parar: ')