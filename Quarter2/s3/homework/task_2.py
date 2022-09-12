# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint


def create_rand_list(_size, _span):
    return [randint(-_span, _span) for _ in range(_size)]


def multiply_pairs(_list, _size):
    return [_list[i] * (_list[_size - i - 1]) for i in range((_size + 1)//2)]


size = 7
span = 10

list1 = create_rand_list(size, span)
print(f'generated list: {list1}')
print(f'multipling pairs: {multiply_pairs(list1,size)}')
