import pygame
import random
import sys

pygame.init()
size = width, height = 800, 800
black = 0, 0, 0
yellow = 248, 255, 43
tamanho = 50

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tarefa 8')

screen.fill(black)

font = pygame.font.SysFont('Comic Sans', 40, bold=False, italic=False)
font_surface = font.render('Clique', True, black)
pygame.draw.circle(screen, yellow, (405, 110), 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.update()
    screen.blit(font_surface, [360, 100])
