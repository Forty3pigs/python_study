KEYS = ['lastname', 'name', 'phone']
db_path = "./data/data.db"
messages = [
    'commands:\n/find, /import, /export, /commands ',
    'input: ',
    'help text',
    '/find принимает запрос на поиск пользователя в базе. Формат: "/find name Иван", где name - название поля таблицы\n'
    f'доступные поля: {KEYS}\nБез параметров выводит всю базу\n'
    '/import - импортирует данные из файла в таблицу. Формат: "/import имя_файла", форматы txt,csv\n'
    '/export - экспорт данных из базы.'
    'формат тот же, имя файла не обязательно. По умолчанию экспорт в файл output.txt',
]
