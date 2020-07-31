import pygame
from Battle_City.settings import *
from Battle_City.models import *


pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
bg = pygame.image.load('1.jpg').convert()
bg_rect = bg.get_rect()
pygame.display.set_caption("Game_one")

pl = Player()
pl2 = Enemy()
tanks = pygame.sprite.Group()
tanks.add(pl2)


def win_draw():
    win.blit(bg, bg_rect)
    win.blit(pl.image, pl.rect)
    # win.blit(pl2.image,  pl2.rect)
    tanks.draw(win)
    pygame.display.update()


def display_text():
    GAME_FONT = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = GAME_FONT.render('GAME OVER', False, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = WIN_WIDTH / 2
    text_rect.top = 10
    win.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.delay(3000)


play = True
# Цикл выполняется пока переменная равна True
while play:
    pygame.time.delay(10)  # 0.1 second`s
    for smth_event in pygame.event.get():
        if smth_event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    pl.move_player(keys)
    pl2.move_enemy(keys)
    collide = pygame.sprite.spritecollide(pl, tanks, False)
    if not collide:
        win_draw()
    else:
        display_text()
        play = False

# pygame.quit()
