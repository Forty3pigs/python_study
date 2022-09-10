# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

def sum_number_digits(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    return sum


def input_to_digits_only(input_string):
    digit_string = ''
    for i in input_string:
        if i.isdigit():
            digit_string += i
    return int(digit_string)


try:
    input = input('enter your number(float): ')
    sum = sum_number_digits(input_to_digits_only(input))
    print(f'sum of digits of {input} is {sum}')
except:
    print('wrong input')
