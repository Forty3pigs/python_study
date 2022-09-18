# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

some_list = [int(input()) for _ in range(int(input()))]
new_list = []
for i in range(len(some_list) // 2 + len(some_list) % 2):
    new_list.append(some_list[i] * some_list[len(some_list) - 1 - i])
print(new_list)
