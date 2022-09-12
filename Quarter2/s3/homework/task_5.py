# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def pFib(n):
    lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst


def nFib(n):
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append(lst[i - 2] - lst[i - 1])
    lst.reverse()
    return lst


def Fib(n):
    lst = [None] * (2*n - 2)
    lst = lst[:n-1] + [1, 0, 1] + lst[n-1:]
    for i in range(n + 2, 2 * n+1):
        lst[i] = lst[i - 1] + lst[i - 2]
    for i in range(n, -1, -1):
        lst[i] = lst[i + 2] - lst[i + 1]
    return lst


n = 8

print(nFib(n)+pFib(n))
print(Fib(n))
