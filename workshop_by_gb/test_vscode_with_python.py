# Ищем максимальное число из заданных. Своё. Цикл for. Массив(список)
numbers = [4, 8, 12, 4, 7]
max = numbers[0]

for x in numbers:
    print(x)
    if x > max:
        max = x

print(max)
