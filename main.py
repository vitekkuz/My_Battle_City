import pygame
from Battle_City.settings import *
from Battle_City.models import *


pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
bg = pygame.image.load('1.jpg').convert()
bg_rect = bg.get_rect()
pygame.display.set_caption("Game_one")

pl = Player()

play = True
# Цикл выполняется пока переменная равна True
while play:
    pygame.time.delay(10)  # 0.1 second`s
    for smth_event in pygame.event.get():
        if smth_event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pl.posx > pl.speed:
        pl.posx -= pl.speed
    elif keys[pygame.K_RIGHT] and pl.posx < WIN_WIDTH-pl.speed-pl.width:
        pl.posx += pl.speed
    elif keys[pygame.K_UP] and pl.posy > pl.speed:
        if not pl.direction['move_up']:
            pl.image = pygame.transform.flip(pl.image, False, True)
        pl.posy -= pl.speed
        for n in pl.direction.keys():
            if n == 'move_up':
                pl.direction[n] = True
            else:
                pl.direction[n] = False
    elif keys[pygame.K_DOWN] and pl.posy < WIN_HEIGHT-pl.speed-pl.height:
        if not pl.direction['move_down']:
            pl.image = pygame.transform.flip(pl.image, False, True)
        pl.posy += pl.speed
        for n in pl.direction.keys():
            if n == 'move_down':
                pl.direction[n] = True
            else:
                pl.direction[n] = False

    # drawWindow() не создана
    win.blit(bg, bg_rect)
    win.blit(pl.image, (pl.posx, pl.posy), pl.rect)
    pygame.display.update()

pygame.quit()
