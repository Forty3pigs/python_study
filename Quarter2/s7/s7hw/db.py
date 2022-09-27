import sqlite3 as db
from keys import db_path
import os.path
import txt_csv


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


def read_db(query='*'):
    temp_db = db.connect(db_path)
    temp_db.row_factory = db.Row
    values = temp_db.execute("SELECT " + query + "FROM Users").fetchall()

    list_accumulator = []

    for item in values:
        list_accumulator.append({k: item[k] for k in item.keys()})
    print(list_accumulator)
    temp_db.close()

    return list_accumulator


def drop_db():
    temp_db = db.connect(db_path)
    temp_db.execute('DROP TABLE users')
    temp_db.commit()
    temp_db.close()


create_db()
data = txt_csv.read_file()
write_db(data)

