import pygame
import ram_player
from pygame.locals import *

pygame.init()

WIDTH=950
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ram Setu")

bg=pygame.image.load('Assets/main_bg.png')

player=ram_player.Player(100,HEIGHT-80)

run=True
while run:
    screen.blit(bg, (0,0))
    player.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
    pygame.display.update()
pygame.quit()