# Задана натуральная степень kf. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени kf.

# Пример:

# kf = 2 =>
# 2x² + 4x + 5 = 0 или
# x² + 5 = 0 или
# 10*x² = 0

from eq_func import create_eq_file as cef, get_line_from_file as gl

path = './equation.txt'
cef(int(input('enter k: ')), path)
print(gl(path))
