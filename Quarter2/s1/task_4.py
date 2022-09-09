# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def possible_coord_values(quad):
    if quad == 1:
        return 'x > 0, y >0'
    elif quad == 2:
        return 'x < 0, y > 0'
    elif quad == 3:
        return 'x < 0, y < 0'
    elif quad == 4:
        return 'x > 0, y < 0'
    else:
        return 'wrong input'


try:
    print(possible_coord_values(int(input('enter quarter: '))))
except:
    print('Nein')
