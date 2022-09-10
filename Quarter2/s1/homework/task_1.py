# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def weekend_check(d):
    if d == 6 or d == 7:
        return True
    elif 0 < d < 6:
        return False
    else:
        return None


d = weekend_check(int(input('enter day number: ')))
if d:
    print('Yes')
elif d == False:
    print('No')
else:
    print('Wrong input')
