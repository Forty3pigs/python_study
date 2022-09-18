# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141

from ctypes import resize
from math import pi

# здесь вводится требуемое кол-во знаков после запятой
n = input('accuracy: ').split('.')[1]
print(round(pi, len(n)))

# здесь ввод в формате из примера
input_number = input('number: ')
acc = input('accuracy: ').split('.')[1]

num = input_number.split('.')
ln = len(num[1])
la = len(acc)

if ln == la:
    print(input_number)
elif ln > la:
    print(num[0] + '.' + resize(num[1], la))
else:
    print(input_number + '0'*(la - ln))
