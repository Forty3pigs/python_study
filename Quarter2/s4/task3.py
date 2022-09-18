# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from random import randint as rnd
from math import lcm, gcd


def nod(n, m):
    while (n != m):
        if (n > m):
            n = n - m
        else:
            m = m - n
    return n


def nok(n, m):
    return int(n * m / nod(n, m))


a = int(input('1st: '))
b = int(input('2st: '))
# a = rnd(2, 100)
# b = rnd(2, 100)

print(f'nok = {nok(a, b)}, nod = {nod(a,b)}')
print(f'nok = {lcm(a, b)}, nod = {gcd(a,b)}')
