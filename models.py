'''
    Classes for game models
'''
import pygame
from Battle_City.settings import *


class Player:
    def __init__(self):
        self.image = pygame.image.load('MySprites/tank.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.width = 120
        self.height = 120
        self.posx = 140
        self.posy = WIN_HEIGHT - self.height - 15
        self.speed = 5
        # self.centerx = self.width / 2
        # self.centery= self.height/ 2
        self.direction = {
            'move_up': True,
            'move_right': False,
            'move_down': False,
            'move_left': False,
        }
