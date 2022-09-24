# задача 2 HARD необязательная. Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры).
# Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива,
# причем чтобы каждый гарантированно один раз переместился на другое место и потом не участвовал никак
# (возможно для этого удобно будет использование множества) и выполнить это за m*n / 2 итераций.
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

from func_from_hard_sort import create_2d_list as cl, random_fill_list as rf, print_list as pl
from func_from_hard_sort import first_2d_to_1d_list as l2d
from func_from_hard_sort import vector2matrix as v2m, shuffle_list as sl

x = 5
y = 6

lst = cl(x, y)
lst = rf(lst)
pl(lst)
print()
lst = l2d(lst)
lst = sl(lst)
lst = v2m(lst, x)
pl(lst)

# это по логике, а надо рандомные менять
