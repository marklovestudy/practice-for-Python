import sys

import pygame
s=pygame.display.set_mode((800,600))
s.fill('green')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(s,'red',(100,100,200,100),10)
    pygame.draw.line(s,'yellow',(100,100),(200,100),10)
    pygame.draw.circle(s,'red',(200,200),50,15)
    pygame.draw.arc(s,'red',(300,100,200,100),0,5,15)
    pygame.draw.lines(s,'pink',True,((300,300),(500,400),(400,400),(500,600)),10)
    pygame.draw.ellipse(s,'red',(100,400,200,100),10)
    pygame.draw.aaline(s,'yellow',(500,100),(600,100))
    pygame.draw.aalines(s,'pink',True,((300,400),(500,500),(400,500),(500,700)),10)
    pygame.draw.polygon(s,'pink',((500,300),(600,400),(500,200),(500,400),(600,600)))
    pygame.display.flip()