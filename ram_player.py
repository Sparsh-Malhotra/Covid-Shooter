import pygame
from pygame.locals import *

pygame.init()

WIDTH=950
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))

class Player():
    def __init__(self, x, y):
        img = pygame.image.load('Assets/ram.png')
        self.image = pygame.transform.scale(img, (120,120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):
        dx = 0
        dy = 0

		#get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -20
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 1
        if key[pygame.K_RIGHT]:
            dx += 1.5


		#add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

		#check for collision

		#update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0

		#draw player onto screen
        screen.blit(self.image, self.rect)