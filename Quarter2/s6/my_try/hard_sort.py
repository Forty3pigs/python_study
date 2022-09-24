# Задача HARD SORT.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10


from random import randint


x = 5
y = 6


def create_2d_list(x, y):
    lst = [[0] * x for _ in range(y)]
    return lst


def random_fill_list(l):

    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j] = randint(1, 20)
    return l


# def print_list(l):
#     for i in l:
#         print(' '.join(list(map(str, i))))

def print_list(l):
    for i in l:
        print(''.join(str(i)))


def first_2d_to_1d_list(l):
    l = sum(l, [])
    # print(l)
    return l


def second_2d_to_1d_list(l):
    l = [i for item in l for i in item]
    return l


def vector2matrix(l, x):
    return [l[i:i+x] for i in range(0, len(l), x)]


lst = create_2d_list(x, y)
lst = random_fill_list(lst)
print(lst)
print_list(lst)
lst = first_2d_to_1d_list(lst)
#lst = second_2d_to_1d_list(lst)
lst = sorted(lst)
print(lst)
lst = vector2matrix(lst, x)
print(lst)


# Доп.задача
# перемешать эл-ты массива за len/2 итераций, так, чтобы ни 1 из элементов не перемещался более 1 раза. Эл-тов чётное кол-во

x = 6
lst = [i for i in range(x)]
print(lst)
r = x//2
for i in range(r):
    lst[i], lst[i+r] = lst[i+r], lst[i]
print(lst)