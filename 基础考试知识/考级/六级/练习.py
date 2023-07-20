import sys
import pygame
s=pygame.display.set_mode((800,600))
s.fill('green')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.rect(s,'red',(100,100,50,50),10)
    pygame.draw.circle(s,'red',(200,100),50,10)
    pygame.draw.line(s,'red',(200,100),(300,100),15)
    pygame.draw.lines(s,'yellow',True,((300,100),(300,200),(400,100),(400,200)),10)
    pygame.draw.arc(s,'black',(100,200,200,100),0,3,15)
    pygame.draw.polygon(s,'pink',((300,300),(300,400),(400,300),(400,400)))
    pygame.draw.aalines(s,'black',True,((300,500),(300,600),(400,500),(400,600)))
    pygame.draw.aaline(s,'pink',(600,500),(800,500))
    pygame.draw.ellipse(s,'pink',(500,300,200,100))
    pygame.display.flip()