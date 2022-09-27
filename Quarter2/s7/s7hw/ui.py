import txt_csv

KEYS = ['Last name', 'Name', 'Phone']

messages = {
    'error': 'error',
    'file_error': 'file error text',
    'intro': 'intro text',
    'help': 'help text',
    'input au': 'input1 text',
    'input af': 'input1 text',
    'success': 'success text',
    'fail': 'fail text'
}


def add_user():
    unchecked_data = input(messages['input au'])
    return unchecked_data


def add_file():
    unchecked_path = input(messages['input af'])
    return unchecked_path


def view_short_help():
    print(messages['help'])


def find_user(key, value, path='data.txt'):
    'поиск в базе по ключу и значению'
    data = txt_input_read(path)
    try:
        return [line for line in data if line[key] == value]
    except:
        return ['No such key']


def print_cleaner(output):
    'очистка вывода данных'
    for dict in output:
        result = ''
        for i in range(len(dict)):
            result += f'{KEYS[i]} {dict[KEYS[i]]}; '
        # походу это проверяет, что последний в output является текущим и последним dict
        if output[-1] == dict:
            # чтобы отрезать последнюю точку с запятой в последней строке вывода
            print(result[:-2])
        else:
            print(result[:-1])
    print()
