import pygame
pygame.init()
print('Desafio 021 - Python - Curso em Video')
print('Tocar MP3!')
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
