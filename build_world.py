import pygame
from pygame.locals import *

pygame.init()
WIDTH=950
HEIGHT=700
tile_width = 38
tile_height=28
screen=pygame.display.set_mode((WIDTH,HEIGHT))

class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('Assets\ps3.png')
        grass_img = pygame.image.load('Assets\ps4.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_width, tile_height))
                    img_rect=img.get_rect()
                    img_rect.x = col_count * tile_width
                    img_rect.y = row_count * tile_height
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_width, tile_height))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_width
                    img_rect.y = row_count * tile_height
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
