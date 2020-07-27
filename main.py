import pygame
from .Get_sprites import get_img

WIN_WIDTH = 800
WIN_HEIGHT = 600

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Game_one")


player_width = 40
player_height = 60
player_posx = 100
player_posy = WIN_HEIGHT-player_height-15
player_speed = 5

isJump = False
jumpCount = 10


play = True
# Цикл выполняется пока переменная равна True
while play:
    pygame.time.delay(20)  # 0.1 second`s
    for smth_event in pygame.event.get():
        if smth_event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_posx > player_speed:
        player_posx -= player_speed
    elif keys[pygame.K_RIGHT] and player_posx < WIN_WIDTH-player_speed-player_width:
        player_posx += player_speed
    if not isJump:
        if keys[pygame.K_UP] and player_posy > player_speed:
            player_posy -= player_speed
        elif keys[pygame.K_DOWN] and player_posy < WIN_HEIGHT-player_speed-player_height:
            player_posy += player_speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                player_posy += (jumpCount ** 2)/1.7
            else:
                player_posy -= (jumpCount ** 2)/1.7
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((14, 0, 10))
    pygame.draw.rect(win, (100, 0, 255), (player_posx, player_posy, player_width, player_height))
    pygame.display.update()

pygame.quit()
