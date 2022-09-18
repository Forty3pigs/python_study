# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]


# my try

with open('f.txt', 'r') as file:
    data_str = file.read().split()
data_int = [int(i) for i in data_str]
res = [(i, i ** 2) for i in data_int if i % 2 == 0]
print(data_int)
print(res)


# lector

# Первый вариант
f = open('f.txt', 'r')
# искуственно добавляем в конце пробел
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    # получаем индекс первого пробела
    space_pos = data.index(' ')
    # добаляем в список всё, что до индекса первого пробела, преобразуя в инт
    numbers.append(int(data[:space_pos]))
    # отрезаем в данных всё до пробела и пробел
    data = data[space_pos+1:]
out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)

# Второй вариант

# ф-ция принимает на фход некую ф-цию и колллекцию


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
# перегоняем список строк в инт при помощи ф-ции
data = select(int, data)
# выбираем из списка чётные при помощи лямбды
data = where(lambda e: not e % 2, data)
# создаём кортежи при помощи лямбды и перегоняем их в список через ф-цию
data = select(lambda e: (e, e**2), data)
print(data)


# иначе и без ф-ций
data = '1 2 3 5 8 15 23 38'.split()
data = map(int, data)
data = filter(lambda e: not e % 2, data)
data = list(map(lambda e: (e, e**2), data))
print(data)
