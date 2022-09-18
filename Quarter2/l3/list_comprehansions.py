# формат выражений
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]


# заполняем список чётными числами от 1 до 20
lst1 = [i for i in range(1, 21) if i % 2 == 0]
print(lst1)
# заполняем список кортежами вида (n, n^2) для чётных чисел
lst2 = [(i, i**2) for i in range(1, 21) if i % 2 == 0]
print(lst2)


def f(x):
    return x**3


# заполняем список кубами чётных чисел от 1 до 20
lst3 = [f(i) for i in range(1, 21) if i % 2 == 0]
print(lst3)
