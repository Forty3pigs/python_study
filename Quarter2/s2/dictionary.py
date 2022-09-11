# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('enter N: '))
n = 6

# просто строкой
for i in range(1, n):
    print(i, ':', 3 * i + 1, end=',  ')
print(n, ':', 3 * n + 1)

# словарь
my_dict = {}
for i in range(1, n+1):
    my_dict[i] = 3 * i + 1
print(my_dict)

# пример работы со словарём:
translate = {'cat': 'кот', 'dog': 'собака', 'monkey': 'обезьяна'}
print(translate['cat'])
translate['cat'] = 'кошка'
print(translate)
translate['girafаe'] = 'жираф'
print(translate)

# более правильно делать с фуункцией:


def func(x):
    return 3*x + 1


my_dict = {}
for i in range(1, n + 1):
    my_dict[i] = func(i)
print(my_dict)
