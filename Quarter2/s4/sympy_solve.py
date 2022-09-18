import sympy as sm
x = sm.Symbol('x')
a = int(input('1st: '))
b = int(input('2st: '))
c = int(input('3st: '))
print(sm.solveset(a*x**2 + b * x + c, x))
