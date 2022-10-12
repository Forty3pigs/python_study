import csv

table = ['last_name', 'name', 'phone_number', 'post', 'salary']


def get_data():
    record = [input(f'{i}: ') for i in table]
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(record)
    print('data added')
    return record
