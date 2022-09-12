# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint


def create_rand_list(_size, _span):
    return [randint(-_span, _span) for i in range(_size)]


def sum_odd_pos(_list, _size):
    return (sum([int(_list[i]) for i in range(1, _size, 2)]))


# list1 = [2, 3, 5, 9, 3]
size = 6
span = 10

list1 = create_rand_list(size, span)
sum_odds = sum_odd_pos(list1, size)
print(f'list: {list1} \nsum of odds positions: {sum_odds}')
