def forming_query(input):
    output = input
    return output


def parser(input_string):
    query = tuple(input_string)
    return query


def check_new(data, path='data.txt'):
    'проверка на уникальность входных данных'
    already_exist = txt_input_read(path)
    return [element for element in data if element not in already_exist]
