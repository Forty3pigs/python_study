# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def get_string_list(_size):
    'список строк пользователя размером size'
    return [input(f'input {_ +1} string: ') for _ in range(_size)]


def find_in_list(_lst, _str):
    for i in _lst:
        if i == _str:
            return True
    return False


size = 4
req_string = input('enter searching number: ')
user_list = get_string_list(4)
print(find_in_list(user_list, req_string))
