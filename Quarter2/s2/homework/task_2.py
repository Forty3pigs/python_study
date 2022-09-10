# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


try:
    n = int(input('enter N: '))
except:
    print('wrong input')

output = []
for i in range(1, n+1):
    output.append(fac(i))
print(output)
