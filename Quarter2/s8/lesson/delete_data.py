import csv


def delete_data():
    request = input('delete: ')
    with open('data.csv', 'w', encoding='UTF-8') as file:
        reader = file.readlines()
        #reader = csv.reader(file, delimiter=',')
        for line in reader:
            if request in line:
                del reader[line]
    return request
