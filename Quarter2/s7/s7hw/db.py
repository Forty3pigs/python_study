import sqlite3 as db
from keys import db_path, KEYS
import os.path


def check_db():
    return os.path.exists(db_path)


def create_db():
    connection = db.connect(db_path)
    cursor = connection.cursor()

    try:
        result = cursor.execute('''
                                CREATE TABLE users (                                
                                lastname TEXT,
                                name TEXT,
                                phone TEXT
                                )
                                ''').fetchall()
    except:
        print('DB already exist')


def write_db(data):
    # сюда можно прикрутить KEYS
    if not check_db():
        create_db()
    temp_db = db.connect(db_path)

    for item in data:
        temp_db.execute('''
                        INSERT INTO users (lastname, name, phone)
                        VALUES(:lastname, :name, :phone)
                        ''',
                        item,
                        )
        temp_db.commit()  # commit after each addition
        # print a helpful message once added
        print(f"Added data {item['lastname']}")

    temp_db.close()


def read_db(query='SELECT * FROM users'):
    if not check_db():
        create_db()
    temp_db = db.connect(db_path)
    temp_db.row_factory = db.Row
    values = temp_db.execute(query).fetchall()

    data = []

    for item in values:
        data.append({k: item[k] for k in item.keys()})
    temp_db.close()

    return data


def drop_db():
    temp_db = db.connect(db_path)
    temp_db.execute('DROP TABLE users')
    temp_db.commit()
    temp_db.close()


def only_new(data):
    'проверка на уникальность входных данных'
    already_exist = read_db()
    if already_exist:
        data = [element for element in data if element not in already_exist]
    return data


def print_cleaner(data):
    'очистка вывода данных'
    for dict in data:
        result = ''
        for i in range(len(dict)):
            result += f'{KEYS[i]} {dict[KEYS[i]]}; '
        # походу это проверяет, что последний в output является текущим и последним dict
        if data[-1] == dict:
            # чтобы отрезать последнюю точку с запятой в последней строке вывода
            print(result[:-2])
        else:
            print(result[:-1])
    print()
