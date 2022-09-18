def sum(x, y):
    return x+y


def calc(op, a, b):         # функция принимает в качестве аргумента функцию
    return op(a, b)


print(calc(sum, 5, 6))

f = sum                     # присвиваем переменной функцию
print(calc(f, 4, 8))


def g(q, w): return q + w


print(g(4, 5))

print(calc(lambda q, w: q+w, 12, 14))
