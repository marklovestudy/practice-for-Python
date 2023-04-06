import sys
import pygame
screen=pygame.display.set_mode((800,600))
head = pygame.image.load('cry.png').convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill('green')
    screen.blit(head,(400,400))
    pygame.display.update()