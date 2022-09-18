# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [int(input(f'{i+1} number: ')) for i in range(int(input('len: ')))]
print(lst)
sum = 0
for i in range(0, len(lst), 2):
    sum += lst[i]
print(f'odds sum is: {sum}')
