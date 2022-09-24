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


OPERATORS = {'*': lambda x, y: x * y, '/': lambda x, y: x / y,
             '+': lambda x, y: x + y, '-': lambda x, y: x - y
             }

task = '20+8/4-13*3'  # 20 + 2 - 39 =  -17
task = task.replace(' ', '')


def parse(expression):
    tmp = ''
    numbers = []
    for char in expression:
        if char not in OPERATORS:
            tmp += char
        else:
            numbers.append(int(tmp))
            numbers.append(char)
            tmp = ''
    numbers.append(int(tmp))
    return numbers


def find_n_solve(op, lst):
    for i in range(0, len(lst)-1):
        if lst[i] == op:
            num1 = lst[i-1]
            num2 = lst[i+1]
            res = OPERATORS[op](num1, num2)
            lst = lst[:i-1] + [res] + nums[i+2:]
            return lst
    return False


nums = parse(task)
print(nums)

for ops in OPERATORS:
    while find_n_solve(ops, nums):
        nums = find_n_solve(ops, nums)

print(nums)
