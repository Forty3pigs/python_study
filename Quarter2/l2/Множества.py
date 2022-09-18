colors = {'red', 'green', 'blue'}
print(type(colors))

colors.add('orange')
colors.remove('blue')       # такой элемент ДОЛЖЕН быть в сете
colors.discard('green')     # а так ошибки не будет, если элемента нет
colors.clear()              # очистка сета

a = {2, 4, 7, 12, 3}
b = {4, 2, 3, 2, 5, 1}
print(f'b = {b}')

c = a.copy()                # c = {2, 4, 7, 12, 3}
u = a.union(b)              # u = u = {1, 2, 3, 4, 5, 7, 12}
i = a.intersection(b)       # i = {2, 3, 4}
dl = a.difference(b)        # dl = dl = {12, 7}
dr = b.difference(a)        # dr = {1, 5}

q = a \
    .union(b) \
    .difference(a.intersection(b))          # q = {1, 12, 5, 7}

f = frozenset(q)            # множество f, равное q, заморожено и неизменно


c = b.copy()
c = c.discard(5)
print(f'c - {type(c)}')
print(f'c = {c}')


print(f'u = {u}')
print(f'i = {i}')
print(f'dl = {dl}')
print(f'dr = {dr}')
print(f'q = {q}')
