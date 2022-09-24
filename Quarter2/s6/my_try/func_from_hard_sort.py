from random import randint


def create_2d_list(x, y):
    lst = [[0] * x for _ in range(y)]
    return lst


def random_fill_list(l):

    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] = randint(1, 20)
    return l


def print_list(l):
    for i in l:
        print(' '.join(list(map(str, i))))


def print_list(l):
    for i in l:
        print(''.join(str(i)))


def first_2d_to_1d_list(l):
    l = sum(l, [])
    return l


def second_2d_to_1d_list(l):
    l = [i for item in l for i in item]
    return l


def vector2matrix(l, x):
    return [l[i:i+x] for i in range(0, len(l), x)]


def shuffle_list_i(l):
    r = len(l)//2
    for i in range(r):
        l[i], l[i+r] = l[i+r], l[i]
    return l



