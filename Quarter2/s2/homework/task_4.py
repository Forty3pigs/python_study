# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


def fill_list(n):
    return [randint(-n, n) for i in range(n)]


def indexes(path):
    with open(path, 'r') as file:
        indexes = [int(line.strip()) for line in file]
    return indexes


def check_indexes(length, indexes):
    for i in indexes:
        index_OK = i < length
    return index_OK


def multi(orig, index):
    mlt = 1
    for i in index:
        mlt *= orig[i]
    return mlt


n = 7
# try:
#     n = int(input('enter N: '))
# except:
#     print('wrong input')
path = 'text.txt'
orig_list = fill_list(n)
index_list = indexes(path)

if check_indexes(len(orig_list), index_list):
    print('\nWARNING: indexes, not numeric position \n')
    print(f'generated list: {orig_list}')
    print(f'resived from file indexes: {index_list}')
    print(f'multiply result: {multi(orig_list, index_list)}\n')
else:
    print('Wrong index in file\n')
