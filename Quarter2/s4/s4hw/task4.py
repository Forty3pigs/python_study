# Задана натуральная степень kf. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени kf.

# Пример:

# kf = 2 =>
# 2x² + 4x + 5 = 0 или
# x² + 5 = 0 или
# 10*x² = 0

from random import randint as rnd
import sympy as sm

x = sm.Symbol('x')


def get_ratio(kf):
    r = [rnd(0, 101) for _ in range(kf)]
    r.insert(0, rnd(1, 101))
    return r
    return str(r)[1:-1]


def form_eq(kf, rat):
    eq = []
    while kf > 0:
        if rat[-kf-1] == 0:
            kf -= 1
            continue

        elif rat[-kf-1] == 1:
            if kf == 1:
                eq += [str(x)]
            else:
                eq += [str(x ** kf)]
        else:
            if kf == 1:
                eq += [str(rat[-kf-1] * x)]
            else:
                eq += [str(rat[-kf-1] * x ** kf)]
        kf -= 1

    if rat[-kf] != 0:
        eq += [str(rat[-kf])]
    eq = ' + '.join(eq)
    eq += ' = 0'

    return eq


def write_to_file(path, eq):
    with open(path, 'w') as file:
        file.write(eq)


def create_eq_file(kf, path):
    _r = get_ratio(kf)
    _eq = form_eq(kf, _r)
    write_to_file(path, _eq)


k = 4
#ratio = [1, 1, 3, 1, 0]
path = './equation.txt'
ratio = get_ratio(k)
equation = form_eq(k, ratio)
write_to_file(path, equation)


#equation = str(form_eq(kf, ratio))[1:-1]
print(ratio)
print(equation)


# def form_eq(kf, rat):
#     eq = []
#     for i in range(kf, -1, -1):
#         if rat[kf-i] == 0:
#             continue
#         elif rat[kf-i] == 1 and i == 0:
#             eq += [str(rat[kf-i])]

#             # elif i == 1:
#             #     eq += ['x']
#             # else:
#             #     [str(rat[kf-i]) + '*x^' + str(i)]
#         else:
#             eq += [str(rat[kf-i]) + '*x^' + str(i)]

#     return eq


# def form_eq(kf, rat):
#     eq = ''
#     for i in range(kf, -1, -1):
#         if rat[kf-i] == 0:
#             continue
#         else:
#             eq += str(rat[kf-i]) + '*x^' + str(i) + ' + '

#             eq = eq.replace('1*x', 'x') \
#                 .replace('x^1', 'x') \
#                 .replace('*x^0 +', ' = 0')
#     return eq


# def form_eq(kf, rat):
#     rat = rat[::-1]
#     eq = '0 = '
#     for i in range(kf):
#         eq += str(i) + '^x*' + str(rat[i-kf]) + " + "
#     return eq[::-1]
