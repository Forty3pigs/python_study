# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def input_coords(n):
    xyz = ['X', 'Y', 'Z']
    a = []
    for i in range(n):
        a.append(
            float(input(f'enter {xyz[i]} for point : ').replace(',', '.')))
    return a


def points_distance(pointA, pointB):
    d = ((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)**0.5
    return d


try:
    print('enter coordinates for point A: ')
    A = input_coords(2)
    print(A)
    print('enter coordinates for point B: ')
    B = input_coords(2)
    print(B)
    distance = round(points_distance(A, B), 3)
    print()
    print(f'distance betwin point A {A} and point B {B} is {distance}')
except:
    print('wrong input')
