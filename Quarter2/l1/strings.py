
text = 'съешь ещё этих мягких французских булок'
print(len(text))                        # 39
print('ещё' in text)                    # True
print(text.isdigit())                   # False
print(text.islower())                   # True
print(text.replace('ещё', 'ЕЩЁ'))


print(text[0])                          # c
print(text[1])                          # ъ
print(text[len(text)-1])                # к                 последний индекс
print(text[-5])                         # б                 пятая буква с конца
print(text[:])                          # print(text)
print(text[:2])                         # съ                первые две буквы
print(text[len(text)-2:])               # ок                последние две буквы
# ешь ещё           с первой по девятую буквы
print(text[2:9])
# ещё этих мягких   с шестой буквы до -18 с конца
print(text[6:-18])
# сеикакл           каждая 6я буква начиная с 0
print(text[0:len(text):6])
print(text[::6])                        # сеикакл           каждая 6я буква
text = text[2:9] + text[-5] + text[:2]  # ...
print(text)

# просто для наглядности индексов
text = 'съешь ещё этих мягких французских булок'
n = 0
for i in text:
    print(n, i)
    n += 1

# вывод текста из for в строку, а не в столбик:
for i in text:
    print(i, end='  ')
print()

# выведите 1 цифру после разделительной точки введённого числа:
number = '4.242'  # имитация ввода
if '.' in number:
    print(number[number.index('.')+1])
else:
    print('no')
