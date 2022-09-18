# Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

input_string = input('numbers sep by space: ')


def max_min_input(string):
    a = [int(i) for i in string.split()]
    return max(a), min(a)


print(max_min_input(input_string))
