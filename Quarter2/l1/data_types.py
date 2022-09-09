# можно выполнить отдельный блок кода: выделяем, Shift+Enter
print('hello')

# типы данных: boolean, int, float, str, list, None
b = True
i = 123
f = 2.234
# для объявления пустой переменной:
n = None
# print(type(c))
#c = 555
# print(type(a))
# print(type(b))
# print(type(c))
s = 'it\'s a string'
print(i, ' - ', b, ' - ', s)
print()
print('{} - {} - {}'.format(f, b, s))
print('{1} - {2} - {0}'.format(f, b, s))  # меняем порядок
print()
print(f'{n} - {s} - {b}')  # None можно выводить

list = []
print(list)

list = ['1', '2', '3']
# можно даже запятую в конце забыть - прокатит
# смесь типов сработает, но делать так моветон
col = ['hell', 1, 132, 5.321, True, ]
print(list, col)
