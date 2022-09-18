# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

from math import *


def simple(n):
    if n > 2:
        _lst = [2]
        for i in range(3, int(sqrt(n)) + 1, 2):
            # пробегаем по списку (lst) простых чисел
            for j in _lst:
                if i % j == 0:
                    break
            else:
                _lst.append(i)
        return(_lst)
    elif n > 0:
        return []


def dividers(n, lst):
    if not lst == None:
        _div = []
        for i in lst:
            if n % i == 0:
                _div.append(i)
            else:
                continue
        if _div == []:
            return 'simple'
        return _div
    else:
        return 'invalid data'


n = int(input('number: '))

s = simple(n)
d = dividers(n, s)
print(d)
