numbers = [1, 2, 3, 4, 5]
print(numbers)                  # [1, 2, 3, 4, 5]

numbers = list(range(1, 6))
print(numbers)                  # [1, 2, 3, 4, 5]

numbers[0] = 10
print(numbers)                  # [10, 2, 3, 4, 5]

for i in numbers:
    i *= 2                      # изменяется переменная, но не сам список
    print(i)                    # [20, 4, 6, 8, 10]
print(numbers)                  # [10, 2, 3, 4, 5]
print()

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)                    # red green blue
print()

for e in colors:
    print(e*2)                  # redred greengreen blueblue
print()

colors.append('gray')           # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # True

colors.remove('red')            # удалить элемент по содержимому
print(colors)

del colors[0]                   # удалить элемент по индексу
print(colors)
