from random import randint

m = int(input('columns: '))
n = int(input('rows: '))
matrix = [[randint(0, 9) for i in range(m)] for _ in range(n)]
print(matrix)


def sort():
    global matrix
    new_list = [i for sublist in matrix for i in sublist]
    new_list.sort()
    print(new_list)


def print_list():
    global matrix, n
    for i in range(n):
        print(*matrix[i], end='\n')


print_list()
