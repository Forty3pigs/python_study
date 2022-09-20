print('Введите а: ')
a = input()
print('Введите b: ')
b = input()
print(a, b)
print(a, '+', b, '=', a + b)  # получим конкатенацию строк, вместо вычисления
# a = int(a)
# b = int(b)
a = float(a)
b = int(b)
# после перевода в int получим уже вычисление, конвертить можно сходу входные данные
# при корректном вводе float и int нормально складываются
print(a, '+', b, '=', a + b)

i, b, s, f, n = 5
print(i, ' - ', b, ' - ', s)
print()
print('{} - {} - {}'.format(f, b, s))
print('{1} - {2} - {0}'.format(f, b, s))  # меняем порядок
print()
print(f'{n} - {s} - {b}')  # None можно выводить
