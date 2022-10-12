# . Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
# с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate(num):
    dict_nums = {
        'one':'один',
        'two' :'два',
        'three' : 'три',
        'four':'четыре',
        'five':'пять',
        'six':'шесть',
        'seven':'семь',
        'eight':'восемь',
        'nine':'девять',
        'ten':'десять'
    }
    if num[0].islower():
        return dict_nums.get(num, 'invalid key')
    else:
        return dict_nums.get(num.lower(), 'invalid key').title()

print(num_translate('one'))
print(num_translate('Two'))
print(num_translate('Tw'))