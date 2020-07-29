import pygame

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
move_up = True
move_right = False
move_down = False
move_left = False


def drawWindow():
    # pl = pygame.image.load('1.jpg').convert()
    # pl_rect = pl.get_rect()
    # win.blit(pl, pl_rect)

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (100, 0, 255), (player_posx, player_posy, player_width, player_height))
    pygame.display.update()


play = True
# Цикл выполняется пока переменная равна True
while play:
    pygame.time.delay(10)  # 0.1 second`s
    for smth_event in pygame.event.get():
        if smth_event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_posx > player_speed:
        player_posx -= player_speed
    elif keys[pygame.K_RIGHT] and player_posx < WIN_WIDTH-player_speed-player_width:
        player_posx += player_speed
    elif keys[pygame.K_UP] and player_posy > player_speed:
        player_posy -= player_speed
    elif keys[pygame.K_DOWN] and player_posy < WIN_HEIGHT-player_speed-player_height:
        player_posy += player_speed

    drawWindow()


pygame.quit()
