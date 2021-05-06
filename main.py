import pygame
from pygame.locals import *

pygame.init()

WIDTH=950
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ram Setu")

bg=pygame.image.load('Assets/main_bg.png')

run=True
while run:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
    pygame.display.update()
pygame.quit()