# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

try:
    n = int(input('enter number: '))
except:
    print('wrong input')
print(f'binary of {n} is {bin(n)[2:]}')
