import pygame
from build_world import *
from pygame.locals import *

pygame.init()
WIDTH=950
HEIGHT=700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
img = pygame.image.load('Assets/ram.png')
revImg = pygame.transform.flip(img,True,False)

class Player():
    def __init__(self, x, y,obj1):
        self.obj1=obj1
        self.image = pygame.transform.scale(img, (120,120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width=self.image.get_width()
        self.height=self.image.get_height()
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
            self.image = pygame.transform.scale(revImg, (120,120))
            dx -= 3.5
        if key[pygame.K_RIGHT]:
            self.image = pygame.transform.scale(img, (120,120))
            dx += 3.5


		#add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

		#check for collision
        for tile in self.obj1.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
			#check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if below the ground i.e. jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
				#check if above the ground i.e. falling
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0

		#update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0

		#draw player onto screen
        screen.blit(self.image, self.rect)