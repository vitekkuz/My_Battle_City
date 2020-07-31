'''
    Classes for game models
'''
import pygame
from Battle_City.settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('MySprites/tank.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.width = 120
        self.height = 120
        self.rect.x = 40
        self.rect.y = WIN_HEIGHT - self.height - 15
        self.speed = 5
        # self.centerx = self.width / 2
        # self.centery= self.height/ 2
        self.direction = [
            ['move_up', True],
            ['move_right', False],
            ['move_down', False],
            ['move_left', False],
        ]
    
    def move_player(self, keys):
        dir_delta = 0

        # move to LEFT
        if keys[pygame.K_LEFT] and self.rect.x > self.speed:
            self.rect.x -= self.speed
            if not self.direction[3][1]:
                for n in range(4):
                    if self.direction[n][1]:
                        dir_delta = n + 1 - 4
                self.image = pygame.transform.rotate(self.image, dir_delta * 90)
                for n in range(4):
                    if self.direction[n][0] == 'move_left':
                        self.direction[n][1] = True
                    else:
                        self.direction[n][1] = False

        # move to RIGHT
        elif keys[pygame.K_RIGHT] and self.rect.x < WIN_WIDTH - self.speed - self.width:
            self.rect.x += self.speed

            if not self.direction[1][1]:
                for n in range(4):
                    if self.direction[n][1]:
                        dir_delta = n + 1 - 2
                self.image = pygame.transform.rotate(self.image, dir_delta * 90)
                for n in range(4):
                    if self.direction[n][0] == 'move_right':
                        self.direction[n][1] = True
                    else:
                        self.direction[n][1] = False

        elif keys[pygame.K_UP] and self.rect.y > self.speed:
            self.rect.y -= self.speed

            if not self.direction[0][1]:
                for n in range(4):
                    if self.direction[n][1]:
                        dir_delta = n + 1 - 1
                self.image = pygame.transform.rotate(self.image, dir_delta * 90)

                for n in range(4):
                    if self.direction[n][0] == 'move_up':
                        self.direction[n][1] = True
                    else:
                        self.direction[n][1] = False

        elif keys[pygame.K_DOWN] and self.rect.y < WIN_HEIGHT - self.speed - self.height:
            self.rect.y += self.speed

            if not self.direction[2][1]:
                for n in range(4):
                    if self.direction[n][1]:
                        dir_delta = n + 1 - 3
                self.image = pygame.transform.rotate(self.image, dir_delta * 90)

                for n in range(4):
                    if self.direction[n][0] == 'move_down':
                        self.direction[n][1] = True
                    else:
                        self.direction[n][1] = False


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('MySprites/enemy.png').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.width = 120
        self.height = 120
        self.rect.x = 440
        self.rect.y = WIN_HEIGHT - self.height - 115
        # self.rect.bottom = 440
        # self.rect.centerx = WIN_HEIGHT - self.height - 215
        # self.posx = 440
        # self.posy = WIN_HEIGHT - self.height - 215
        self.speed = 5
        self.direction = [
            ['move_up', True],
            ['move_right', False],
            ['move_down', False],
            ['move_left', False],
        ]

    def move_enemy(self, keys):
        dir_delta = 0

        # move to LEFT
        if keys[pygame.K_a] and self.rect.x > self.speed:
            self.rect.x -= self.speed
            if not self.direction[3][1]:
                for n in range(4):
                    if self.direction[n][1]:
                        dir_delta = n + 1 - 4
                self.image = pygame.transform.rotate(self.image, dir_delta * 90)
                for n in range(4):
                    if self.direction[n][0] == 'move_left':
                        self.direction[n][1] = True
                    else:
                        self.direction[n][1] = False

        # move to RIGHT
        elif keys[pygame.K_d] and self.rect.x < WIN_WIDTH - self.speed - self.width:
            self.rect.x += self.speed

            if not self.direction[1][1]:
                for n in range(4):
                    if self.direction[n][1]:
                        dir_delta = n + 1 - 2
                self.image = pygame.transform.rotate(self.image, dir_delta * 90)
                for n in range(4):
                    if self.direction[n][0] == 'move_right':
                        self.direction[n][1] = True
                    else:
                        self.direction[n][1] = False

        elif keys[pygame.K_w] and self.rect.y > self.speed:
            self.rect.y -= self.speed

            if not self.direction[0][1]:
                for n in range(4):
                    if self.direction[n][1]:
                        dir_delta = n + 1 - 1
                self.image = pygame.transform.rotate(self.image, dir_delta * 90)

                for n in range(4):
                    if self.direction[n][0] == 'move_up':
                        self.direction[n][1] = True
                    else:
                        self.direction[n][1] = False

        elif keys[pygame.K_s] and self.rect.y < WIN_HEIGHT - self.speed - self.height:
            self.rect.y += self.speed

            if not self.direction[2][1]:
                for n in range(4):
                    if self.direction[n][1]:
                        dir_delta = n + 1 - 3
                self.image = pygame.transform.rotate(self.image, dir_delta * 90)

                for n in range(4):
                    if self.direction[n][0] == 'move_down':
                        self.direction[n][1] = True
                    else:
                        self.direction[n][1] = False
