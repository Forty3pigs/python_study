from keys import KEYS
import csv
import sqlite3 as db


def get_extension(path):
    try:
        return str(path.split('.')[-1])
    except:
        print('f_error')
        return False


def read_file(path='./data/data.txt'):
    'получает путь, возвращает data'
    if get_extension(path):
        extension = get_extension(path)

    if extension == 'txt':
        with open(path, 'r', encoding='UTF-8') as f:
            temp = f.read().split('\n')
            f.close()
            data = []
            for elem in temp:
                temp_dict = {}
                person = elem.split(' ')
                for i in range(len(person)):
                    temp_dict[KEYS[i]] = person[i]
                data.append(temp_dict)
            return data

    elif extension == 'csv':
        with open(path) as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                data.append(row)
        return data


# def write_file(path = 'output.txt', data):
#     extension = get_extension(path)
#     if extension == 'txt':
#     elif extension == 'csv':


# path1 = '.\data\data.txt'
# path2 = '.\data\data.csv'

# print(read_file(path1))
# print(read_file(path2))
