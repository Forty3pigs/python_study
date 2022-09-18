# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("Inset k: "))

fibonacciList = [0]*(k*2+1)
fibonacciList[k] = 0
fibonacciList[k+1] = 1

for i in range(k+2, len(fibonacciList)):
    fibonacciList[i] = fibonacciList[i-2]+fibonacciList[i-1]

for i in range(k, -1, -1):
    fibonacciList[i] = fibonacciList[i+2]-fibonacciList[i+1]

print(fibonacciList)
