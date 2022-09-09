
# if-elif-else
a = 3  # int(input('a = '))
b = 5  # int(input('b = '))
if a > b:
    print('max = ', a)
elif a < b:
    print('max = ', b)
else:
    print('a = b =', a)

# while на примере инвертирования числа
original = 413
inverted = 0
while original != 0:
    inverted = inverted*10 + (original % 10)
    original //= 10
# блок else выполняется после окончания работы основного цикла
else:
    print('ready')
print(inverted)

# цикл for
for i in 1, 2, 3, 4, 5, 6:
    print(i, ' - ', i**2)
print()

n = 2  # старт включительно
m = 10  # окончание НЕ включительно
e = 2  # приращение
r = range(n, m, e)  # сoздаёт энумератор от n до m с шагом e
# или сразу же for i in range(n, m, e)
for i in r:
    print(i, ' - ', i**2)
print()

str = 'qwe - rty'
for i in str:
    print(i)
print()

# вложенные циклы: квадрат из звёздочек 5х5
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
