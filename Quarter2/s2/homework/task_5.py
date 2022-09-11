# Реализуйте алгоритм перемешивания списка.
from random import randint


def create_rand_list(size, n):
    return [randint(-n, n) for i in range(size)]


def shuffle_list(list, size):
    for i in range(size):
        p = randint(0, size - 1)
        list[i], list[p] = list[p], list[i]
    return list


size = 7
span = 550

# size = int(input('size: '))
# span = int(input('span: '))

orig_list = create_rand_list(size, span)
res_list = orig_list.copy()
res_list = shuffle_list(res_list, size)

print(f'\noriginal {orig_list}')
print(f'shuffled {res_list}\n')
