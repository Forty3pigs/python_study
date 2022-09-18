# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from eq_func import create_eq_file as cf, get_line_from_file as gl
from random import randint as rnd
from sympy import *


path1 = './polynom1.txt'
path2 = './polynon2.txt'

# cf(rnd(1, 5), path1)
# cf(rnd(1, 5), path2)


x = Symbol('x')

eq1 = gl(path1)
eq2 = gl(path2)
print(eq1)
print(eq2)

t1 = eq1.strip().split(' + ')
t2 = eq2.strip().split(' + ')
# t = t1[-1]
# print(type(t))
# print(f't1 {t1}')
# print(f't1[-1] {t1[-1]}')
# if t.endswith(' = 0'):
#     t1[-1].replace(' = 0', '')
print(t1)
print(t2)

print(t1[0])
pos_x1 = t1[0].find('x')
pos_x2 = t2[0].find('x')
print(f'posx1 = {pos_x1}')
print(f'posx2 = {pos_x2}')


# def get_ratio(_str, _posx):


def get_degree(_str, _pos):
    if _pos != len(_str):

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
