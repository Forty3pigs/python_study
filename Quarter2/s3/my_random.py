# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from time import *


def my_rnd(start, end):
    n = len(str(end))
    sup = str(time())[-n:]
    sup = int(sup)

    if (sup >= start and sup <= end):
        return sup
    else:
        while (sup < start or sup > end):
            while(sup > end):
                sup -= end//2
            while (sup < start):
                sup += start*2
        return sup


d = [int(x) for x in input('enter min and max separates by space: ').split()]
r = my_rnd(d[0], d[1])
print(r)
