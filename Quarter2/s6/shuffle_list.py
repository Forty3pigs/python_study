from random import randint
from random import choice

m = int(input('columns: '))
n = int(input('rows: '))

initList = []
tempList = []

# тут создаётся рандомный 2D список и параллельно он же в 1D
for i in range(n):
    sp = []
    for j in range(m):
        sp.append(randint(-10, 10))
        tempList.append(sp[j])
    initList.append(sp)
print(initList)
print(tempList)

# создаётся список индексов от нуля до м*н
indexList = [0] * m*n
for i in range(m*n):
    indexList[i] = i

# проход до половины. с помощью choise берём из индексЛиста случайный элемент и сразу оттуда удаляем.
# таким образом за 1 проход у нас вылетают 2 индекса и свапается темпЛист
for i in range(m*n/2):
    a = choice(indexList)
    indexList.remove(a)
    b = choice(indexList)
    indexList.remove(b)
    tempList[a], tempList[b] = tempList[b], tempList[a]

resultList = []
print(tempList)

# перевод обратно из 1D в 2D массив
for i in range(n):
    sp = []
    for j in range(m):
        sp.append(tempList[0])
        tempList.remove(tempList[0])
    resultList.append(sp)

print(resultList)
