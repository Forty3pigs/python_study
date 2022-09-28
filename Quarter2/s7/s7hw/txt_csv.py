from keys import KEYS
import csv
import os.path


def get_extension(path):
    try:
        return str(path.split('.')[-1])
    except:
        print('f_error')
        return False


def check_file(path):
    return os.path.exists(path)


def read_file(path='./data/data.txt'):
    'получает путь, возвращает data'
    if not check_file(path):
        return 'no such file'
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
        with open(path, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                data.append(row)
        return data


def write_file(data, path='output.txt'):
    # if not check_file(path):
    #     return 'no such file'

    extension = get_extension(path)
    if extension == 'txt':
        f = open(path, 'w', encoding='UTF-8')
        temp = ''
        # f.write('test\n')
        for lines in data:
            for element in lines:
                temp += str(lines[element]) + ' '
            temp = temp[:-1] + '\n'
        f.write(temp[:-1])
        f.close()

    elif extension == 'csv':
        with open(path, 'w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for d in data:
                writer.writerow(d)


# path1 = '.\data\data.txt'
# path2 = '.\data\data.csv'

# print(read_file(path1))
# print(read_file(path2))


# data = read_file()
# write_db(data)
