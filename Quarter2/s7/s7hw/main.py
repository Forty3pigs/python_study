# DATA fe
# Иванов Иван +712345
# Семенов Семен +734567
# Матвеев Матвей +756789
# Сидоров Дмитрий +712377
# Григорьев Станислав +799875
import os.path

KEYS = ['Last name', 'Name', 'Phone']


def txt_input_read(path):
    'чтение из файла TXT'
    try:
        f = open(path, 'r', encoding='UTF-8')
    except:
        print('Input does not exist')
        exit()
    temp = f.read().split('\n')
    f.close()
    lines = []
    for elem in temp:
        temp_dict = {}
        person = elem.split(' ')
        for i in range(len(person)):
            temp_dict[KEYS[i]] = person[i]
        lines.append(temp_dict)
    return lines


def txt_add_data(data, path='data.txt'):
    'добавление новых данных в TXT'
    if os.path.getsize(path) == 0:
        temp = ''
    else:
        temp = '\n'
    f = open(path, 'a', encoding='UTF-8')
    new_data = only_new(data)
    for lines in new_data:
        for element in lines:
            temp += str(lines[element])+' '
        temp = temp[:-1] + '\n'
    f.write(temp[:-1])
    f.close()


def only_new(data, path='data.txt'):
    'проверка на уникальность входных данных'
    already_exist = txt_input_read(path)
    return [element for  element in data if element not in already_exist]






#add_data(input_read('input.txt'))
print_cleaner(pull_line('Name', 'Иван'))
