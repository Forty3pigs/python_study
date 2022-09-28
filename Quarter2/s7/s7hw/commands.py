from txt_csv import *
from keys import *
from db import *


def add_user(query):
    write_db(query)
    print('success')


def make_request(query):
    read_db(query)
    print('success')


def view_commands():
    print(messages[3])


def import_file(path):
    data = only_new(read_file(path))
    write_db(data)
    print('success')


def export_file(path='output.txt'):
    data = read_db()
    write_file(data, path)
    print('success')


def find_user(query):
    'поиск в базе по ключу и значению'
    data = read_db(query)
    try:
        print_cleaner(data)
    except:
        return ['No such key']





