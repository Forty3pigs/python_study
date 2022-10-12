from datetime import datetime


def write_log(data, mode):
    if mode == 'w':
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f'Запись данных в {datetime.now()} : {data}\n')
    elif mode == 'r':
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f'Поиск данных в {datetime.now()} : {data}\n')
    elif mode == 'd':
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f'Удаление данных в {datetime.now()} : {data}\n')