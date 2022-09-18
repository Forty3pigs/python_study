from importlib.resources import path
from eq_func import create_eq_file as cf
from random import randint as rnd
from sympy import *


path1 = './polynom1.txt'
path2 = './polynon2.txt'

cf(rnd(1, 5), path1)
cf(rnd(1, 5), path2)
# task4.create_eq_file(rnd(1, 5), path1)
# task4.create_eq_file(rnd(1, 5), path2)

x = Symbol('x')


def get_from_file(path):
    with open(path, 'r') as file:
        return file.readline()


print(get_from_file(path1))
print(get_from_file(path2))

# path = 'text.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
