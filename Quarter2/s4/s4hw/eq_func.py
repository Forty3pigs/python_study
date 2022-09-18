from random import randint as rnd
import sympy as sm

x = sm.Symbol('x')


def get_ratio(kf):
    r = [rnd(0, 101) for _ in range(kf)]
    r.insert(0, rnd(1, 101))
    return r

def form_eq(kf, rat):
    eq = []
    while kf >= 0:
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

    # if rat[-kf] != 0:
    #     eq += [str(rat[-kf])]
    eq = ' + '.join(eq)
    eq += ' = 0'

    return eq


def write_to_file(path, eq):
    with open(path, 'w') as file:
        file.write(eq)

def get_line_from_file(path):
    with open(path, 'r') as file:
        return file.readline()


def create_eq_file(kf, path):
    _r = get_ratio(kf)
    _eq = form_eq(kf, _r)
    write_to_file(path, _eq)