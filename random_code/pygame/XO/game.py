import sys
from time import sleep
import pygame


def scaling(img):
    'Изменение размера картинки под размер окна, если необходимо'
    size = screen.get_size()
    if img.get_size() == size:
        return img
    else:
        img = pygame.transform.scale(img, size)
        return img


def check_win(mas, sign, cols):
    'Проверка на победу/конец игры'
    # заводим переменную для проверки оставшихся нулей (не закончилось ли место / игра)
    zeros = 0
    # проверяем строки на 3 одинаковых
    for row in mas:
        # при проходе по массиву считаем нули и пишем в zeroes
        zeros += row.count(0)
        if row.count(sign) == 3:
            return sign + ' wins'
    # проверяем столбцы на 3 одинаковых
    for col in range(cols):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign + ' wins'
    # проверяем главную диагональ
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign + ' wins'
    # проверяем вторую диагональ
    if mas[2][0] == sign and mas[1][1] == sign and mas[0][2] == sign:
        return sign + ' wins'
    if zeros == 0:
        return 'Tie'
    return False


pygame.init()
SIZE_BLOCK = 100
ROWS = 3
COLS = 3
MARGIN = 15
width_window = SIZE_BLOCK*COLS + MARGIN*(COLS + 1)
height_window = SIZE_BLOCK*ROWS + MARGIN*(ROWS + 1)

size_window = (width_window, height_window)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Ultimate Battle XO')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
splash = pygame.image.load('win2.png')
splash = scaling(splash)


print(screen.get_size())
print(splash.get_size())
print(size_window)
print(type(splash))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

mas = [[0]*COLS for _ in range(ROWS)]
query = 0           # 1, 2, 3, 4, 5 , 6, 7 , 8 для проверки очередности хода
game_over = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (SIZE_BLOCK + MARGIN)
            row = y_mouse // (SIZE_BLOCK + MARGIN)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        # Перезапуск Пробелом через обнуление переменных
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_over) or (
                event.type == pygame.MOUSEBUTTONDOWN and game_over):

            screen.blit(splash, (0, 0))
            pygame.display.update()
            sleep(2)
            screen.fill(BLACK)
            mas = [[0]*COLS for _ in range(ROWS)]
            query = 0
            game_over = False

    if not game_over:
        for row in range(ROWS):
            for col in range(COLS):
                if mas[row][col] == 'x':
                    color = RED
                elif mas[row][col] == 'o':
                    color = GREEN
                else:
                    color = WHITE
                x = col * SIZE_BLOCK + (col + 1) * MARGIN
                y = row * SIZE_BLOCK + (row + 1) * MARGIN
                # рисуем прямоугольник (где рисуем, цвет, Х лев. верх, Y лев. верх, ширина п-уг., длина п-уг.)
                pygame.draw.rect(screen, color, (x, y, SIZE_BLOCK, SIZE_BLOCK))
                if color == RED:
                    # рисуем линию (где рисуем, цвет, (Х начала, Y начала) (X конца, Y конца), толщина)
                    pygame.draw.line(screen, WHITE, (x + 25, y + 25),
                                     (x + SIZE_BLOCK - 25, y + SIZE_BLOCK - 25), 15)
                    pygame.draw.line(screen, WHITE, (x + 25, y + SIZE_BLOCK - 25),
                                     (x + SIZE_BLOCK - 25, y + 25), 15)
                if color == GREEN:
                    # рисуем круг (где рисуем, цвет, (Х центра, Y центра), радиус, толщина)
                    pygame.draw.circle(
                        screen, BLACK, (x + SIZE_BLOCK//2, y + SIZE_BLOCK//2), SIZE_BLOCK//3, 10)

    # проверяем окончание. Так как query уже увеличилось после отрисовки хода,
    # уменьшаем его обратно, чтобы проверить чей был ход. Чётные у нас "х"
    if (query-1) % 2 == 0:
        game_over = check_win(mas, 'x', COLS)
    else:
        game_over = check_win(mas, 'o', COLS)

    if game_over:
        screen.fill(BLACK)
        font_lc = pygame.font.SysFont('lucidaconsole', 60, bold=True)
        text1 = font_lc.render(game_over, 1, WHITE)
        text1_rect = text1.get_rect()
        text1_x = screen.get_width()//2 - text1_rect.width//2
        text1_y = screen.get_height()//2 - text1_rect.height//2
        screen.blit(text1, (text1_x, text1_y))

    pygame.display.update()
