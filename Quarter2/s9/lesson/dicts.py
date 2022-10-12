some_dict = {'name' : 'Ivan',
             'lastname' : 'Fedorov',
             'age' : 20,
             'city': 'Moscow'
}

print(some_dict)
print(some_dict['city'])
print(some_dict.get('age'))
print(some_dict.get('ag'))
print(some_dict.get('ag', 'Invalid key'))
print(some_dict.setdefault('address', 'Kovaleva 3'))
print(some_dict.setdefault('age', 'Lasdasdasd'))
print(some_dict)

for i in some_dict:
    print(i)

for i in some_dict.keys():
    print(i)

for i in some_dict.values():
    print(i)

for key, value in some_dict.items():
    print(f'{key} : {value}')

