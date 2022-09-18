# tuple - кортеж - неизменяемый список
from typing import Type


a = (3, 4, 44)
print(a[-1])
b = (3)         # не котреж
print(type(b))

t = tuple(['red', 'green', 'blue'])     # перегоняем список в кортеж
print(f'{t} is {type(t)}')
# распаковываем кортеж в переменные строго по количеству элементов
r, g, b = t
print(f'{r}, {g}, {b} \n')


# dictionary - словарь. Коллекция формата "ключ : значение"

dictionary = {1: 'one', 2: 'two', 3: 'three'}
print(dictionary[1])
print()
# обратный слеш для написания словаря в столбик. Таб после него НЕЛЬЗЯ.
dictionary = \
    {
        'r': 'red',
        'g': 'green',
        'b': 'blue'
    }
for k in dictionary.keys():     # проход по ключам
    print(k)
for v in dictionary.values():   # проход по значениям
    print(v)
