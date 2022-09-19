import pygame

pygame.init()
size = (400, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ultimate Battle XO')
img = pygame.image.load('F3p_logo.png')
pygame.display.set_icon(img)

fontLC = pygame.font.SysFont('lucidaconsole', 48, bold=True)
fontIM = pygame.font.SysFont('impact', 48, bold=True)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SCREEN_BACKGROUND = (16, 64, 16)

xo = fontLC.render('XO', 1, RED, BLUE)
play = fontIM.render('Play', 1, RED, GREEN)
play_width, play_height = play.get_size()
xo_width, xo_height = xo.get_size()
play_coordi = (200 - (play_width//2), 270)
xo_coordi = (175, 480)

# screen.fill(SCREEN_BACKGROUND)

x, y = 175, 480
direct_x = 1
direct_y = 1

FPS = 60
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    clock.tick(FPS)
    screen.fill(SCREEN_BACKGROUND)
    screen.blit(xo, (x, y))
    screen.blit(play, play_coordi)

    x += direct_x
    if (x + xo_width) >= size[0] or x <= 0:
        direct_x = -direct_x

    y += direct_y
    if (y + xo_height) >= size[1] or y <= 0:
        direct_y = -direct_y

    pygame.display.update()
