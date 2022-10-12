import csv

table = ['last_name', 'name', 'phone_number', 'post', 'salary']


def find_data():
    request = input('search: ')
    with open('data.csv', encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if request in line:
                description = dict(zip(table, line))
                for key, value in description.items():
                    print(f'{key} : {value}')
    return request
