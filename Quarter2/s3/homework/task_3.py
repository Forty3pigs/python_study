# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform as uf


def create_rand_list(sz, sp):
    'рандомный список вещественных чисел размером sz в диапазоне от -sp до +sp'
    return [round(uf(-sp, sp), 2) for _ in range(sz)]


def get_reminder(lst):
    'список чисел с обнулённой целой частью'
    return [round(abs(i) % 1, 2) for i in lst]


size = 5
span = 30

list1 = create_rand_list(size, span)
rem = get_reminder(list1)
m1 = min(rem)
m2 = max(rem)
dif = round(abs(m1 - m2), 2)

print(f'\ngenerated list: {list1}')
print(f'min({m1}) and max({m2}) differece = {dif}\n')
