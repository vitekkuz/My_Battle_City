import pygame


# def get_img():

WIN_WIDTH = 800
WIN_HEIGHT = 600

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


sheet = pygame.image.load('tank.png').convert()
# cells = []
# for n in range(2):
#     width, height = (15, 15)
#     rect = pygame.Rect(n*width, 0, width, height)
#     image = pygame.Surface(rect.size).convert()
#     image.blit(sheet, (0, 0), rect)
#     alpha = image.get_at((0, 0))
#     image.set_colorkey(alpha)
#     cells.append(image)
# playerImg = cells[0]
# player = playerImg.get_rect()

sheet.set_colorkey((255, 255, 255))
rect = sheet.get_rect()
rect.center = (320, 240)

# player.center = (320, 240)


play = True
# Цикл выполняется пока переменная равна True
while play:
    pygame.time.delay(20)  # 0.1 second`s
    for smth_event in pygame.event.get():
        if smth_event.type == pygame.QUIT:
            play = False

    # win.blit(playerImg, player)
    win.blit(sheet, rect)
    pygame.display.update()
