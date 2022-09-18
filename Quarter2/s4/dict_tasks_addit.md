d = {'one': 'один', 'two': 'два','three': 'три','four':'четыре', 'five': 'пять','six': 'шесть','seven': 'семь', 'eight':'восемь','nine':'девять','ten': 'десять'}

def: num_translate(en_word)
    en-ru-dict = {'one': 'один', 'two': 'два','three': 'три','four':'четыре', 'five': 'пять','six': 'шесть','seven': 'семь', 'eight':'восемь','nine':'девять','ten': 'десять'}
    if en_word.islower():
        return en_ru_dict.get(en_word, 'НЕТ')          # чтобы выдавала None (здесь "НЕТ") если нет в словаре
    else:
        return en_ru_dict.get(en_word.lower()).title()

print (num-translate('One')) 