# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

names = ("Яков", "Иван", "Мария", "Петр", "Илья", "Павел")

def thesaurus(*args):
    dict = {}
    for i in args:
        if i[0] not in dict.keys():
            dict[i[0]] = []
        dict[i[0]].append(i)
    return dict

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Павел"))
print(thesaurus(*sorted(names)))
print(thesaurus(*(names)))