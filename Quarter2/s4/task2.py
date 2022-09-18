# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# a. с помощью математических формул нахождения корней квадратного уравнения
# b. с помощью дополнительных библиотек Python

# D = b^2 - 4*a*c.

from math import sqrt

def quad_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    print(f'D = {D}')
    if D > 0:
        return [2*c / (-b + sqrt(D)), 2*c / (-b - sqrt(D))]

    elif D == 0:
        return [-b / (2*a)]

    else:
        return [None]

k = (2, 4, 2)
#k = (int(input(f'{i+1} coefficient: ')) for i in range(3))
print(f'{k[0]}x^2 + {k[1]}x + {k[2]} = 0')
res = quad_equation(k[0], k[1], k[2])
print(res)


