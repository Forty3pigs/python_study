# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import randint as rnd

s = 100
r = 20
# s = int(input('span: '))
# r = int(input('range: '))
l = [rnd(0, s) for _ in range(0, r)]
# добавляем заведомо повторное число из 1й половины списка l
l.append(l[rnd(0, len(l)//2)])
print(l)

o = []
for i in l:
    if i not in o:
        o.append(i)
print(o)

# то же самое однострочником
o = []
[o.append(i) for i in l if i not in o]
print(o)

# или можно перевести в множество(и обратно),
# но список будет упорядочен
print(set(l))
