from keys import messages
from commands import *


def get_command(s):
    try:
        if s.split()[0][0] != '/':
            return 0
    except:
        print('wrong command')
    cmd = s.split()[0][1:]
    if cmd == 'find':
        if s.split()[1:]:
            q = [i.lower() for i in s.split()[1:]]
            query = f'SELECT * FROM users WHERE {q[0]}="{q[1].title()}"'
            find_user(query)
        else:
            find_user('SELECT * FROM users')
    elif cmd == 'import':
        query = ' '.join(s.split()[1:])
        import_file(query)
    elif cmd == 'export':
        query = ' '.join(s.split()[1:])
        export_file(query)
    # elif cmd == 'query':
    #     query = s[1:]
    #     make_request(query)
    elif cmd == 'commands':
        view_commands()


# print(get_command('/find name Иван'))
# print(get_command('/import name Иван'))
# print(get_command('/import out.txt'))
# print(get_command('/query name Иван'))
# print(get_command('/query WHERE Name="Иван"'))
# print(get_command('/commands'))
# print(get_command('/import WHERE Name="Иван"'))

# print(find_user(get_command('/find name Иван')))

