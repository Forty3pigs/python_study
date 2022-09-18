# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from eq_func import form_eq as fq, write_to_file as wtf, get_line_from_file as gl
from random import randint as rnd
from numpy import *


path1 = './polynom1.txt'
path2 = './polynon2.txt'

# cf(rnd(1, 5), path1)
# cf(rnd(1, 5), path2)


#x = Symbol('x')

str1 = gl(path1)
str2 = gl(path2)
# print(str1)
# print(str2)

str1 = str1.split('=')[0]
str2 = str2.split('=')[0]

str1 = str1.split("+")
str2 = str2.split("+")

print(str1)
print(str2)


def cr(item):
    'int: [k, degree]'
    item = item.strip()
    xpos = item.find('x')
    if xpos == -1:
        return [int(item), 0]
    elif xpos == 0:
        return [int(item[3:]), 1]
    else:
        if xpos == len(item)-1:
            item = item.split('*x')
            return [int(item[0]), 1]
        else:
            item = item.split('*x**')
            return [int(item[0]), int(item[1])]


d1 = cr(str1[0])[1]
d2 = cr(str2[0])[1]


def get_max_degree(_d1, _d2):
    # _d1 = int(_d1)
    # _d2 = int(_d2)
    if _d1 > _d2:
        return _d1
    else:
        return _d2


k = get_max_degree(d1, d2)
k_list1 = [0]*(k + 1)
k_list2 = k_list1.copy()
sum_list = []  # k_list1.copy()

print(k_list2)


def form_klists(_str, _kl):
    # _kd = []
    for i in _str:
        _kd = cr(i)
        _kl[_kd[1]] = _kd[0]
    return _kl


k_list1 = form_klists(str1, k_list1)
k_list2 = form_klists(str2, k_list2)

print(k_list1)
print(k_list2)


for i in range(len(k_list1)):
    print(k_list1[i] + k_list2[i])
    sum_list.insert(0, k_list1[i] + k_list2[i])

print(sum_list)

path = './polynom_sum.txt'
_eq = fq(k, sum_list)
wtf(path, _eq)
print(gl(path))


# print(t1[0])
# pos_x1 = t1[0].find('x')
# pos_x2 = t2[0].find('x')
# print(f'posx1 = {pos_x1}')
# print(f'posx2 = {pos_x2}')

# def get_ratio(_str, _posx):

# def get_degree(_str, _pos):
#     if _pos != len(_str):

# print(type(t1[0][pos_x1 + 2]))
# print(t1[0][pos_x1 + 3])
# print(type(len(t1[0])))
# t = t1[0]
# if pos_x1 != len(t):
#     c = ''
#     i = pos_x1+3
#     while i < len(t):
#         c += t[i]
#         i += 1

# print(c)

#c += str(i for i in t if i > t[pos_x+2])
