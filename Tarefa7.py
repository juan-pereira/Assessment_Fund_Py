import pygame
import random
import sys

pygame.init()
size = width, height = 800, 800
black = 0, 0, 0
yellow = 248, 255, 43
tamanho = 50

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tarefa 7')

screen.fill(black)

retan = pygame.Rect(random.randint(1, 800), random.randint(1, 800), tamanho, tamanho)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_SPACE] or pygame.mouse.get_pressed()[2]:
            retan = pygame.Rect(random.randint(1, 800), random.randint(1, 800), tamanho, tamanho)

    pygame.draw.rect(screen, yellow, retan)
    pygame.display.update()
