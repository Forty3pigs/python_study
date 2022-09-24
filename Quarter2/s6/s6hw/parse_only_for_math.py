# Задача 41: Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;


OPERAND = ['*', '/', '-', '+']
OPERATORS = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
             '*': lambda x, y: x * y, '/': lambda x, y: x / y}

task = '20+8/4-13*3'  # 20 + 2 - 39 =  -17
task = task.replace(' ', '')


def parse(expression):
    tmp = ''
    numbers = []
    ops = []
    for char in expression:
        if char not in OPERATORS:
            tmp += char
        else:
            numbers.insert(0, int(tmp))
            numbers.append(char)

            tmp = ''
    numbers.insert(0, int(tmp))
    return numbers


nums = parse(task)
print(nums)
# i = len(nums)
# while len(nums) > 1:

nums = list(reversed(nums))
print(nums)
