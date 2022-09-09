

def quarter_of_point(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4


try:
    x = float(input('enter x: ').replace(',', '.'))
    y = float(input('enter y: ').replace(',', '.'))
    print(f'point in {quarter_of_point(x,y)} quarter')
except:
    print('Wrong input')
