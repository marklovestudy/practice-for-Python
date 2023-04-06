import sys
import pygame
screen=pygame.display.set_mode((800,600))
head = pygame.image.load('11.gif').convert()
y=300
x=300
x_v=0
y_v=0
while True:
    pygame.time.Clock().tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_v=-10
            elif event.key == pygame.K_DOWN:
                y_v=10
            elif event.key == pygame.K_LEFT:
                x_v=-10
            elif event.key == pygame.K_RIGHT:
                x_v=10
    x += x_v
    y += y_v
    screen.fill('green')
    screen.blit(head,(x,y))
    pygame.display.update()