# Задача FOOTBALL: (необязательное) Напишите программу, которая принимает на стандартный вход список игр
# футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:

# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# ### __Sample Input:__

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# ### __Sample Output:__

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

import numpy as np


def get_data(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.read().splitlines()
    return data


def check_in(key):
    global comands
    if key not in comands:
        comands[key] = (0, 0, 0, 0, 0)


def results():
    global data, comands    
    for match in data:
        match = match.strip().split(';')
        goals_1 = int(match[1])
        gaols_2 = int(match[3])
        check_in(match[0])
        check_in(match[2])

        if goals_1 > gaols_2:
            comands[match[0]] += WIN
            comands[match[2]] += LOS

        elif goals_1 < gaols_2:
            comands[match[0]] += LOS
            comands[match[2]] += WIN

        else:
            comands[match[0]] += TIE
            comands[match[2]] += TIE


def dict_print(dict):
    for key, value in dict.items():
        value = ' '.join(list(map(str, value)))
        print(f'{key}: {value}')


path = 'football.txt'
data = get_data(path)[1:]
comands = dict()
print(data)

WIN = np.array([1, 1, 0, 0, 3])
TIE = np.array([1, 0, 1, 0, 1])
LOS = np.array([1, 0, 0, 1, 0])


results()
print(comands)
dict_print(comands)
