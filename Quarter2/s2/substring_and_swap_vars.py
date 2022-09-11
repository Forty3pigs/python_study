# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# str1 = input('enter 1st string: ')
# str2 = input('enter 2nd string: ')

str1 = 'В лесу родилась ёлочка, в лесу она росла'
str2 = 'в лесу'
if len(str2) > len(str1):
    str1, str2 = str2, str1
print(str1.lower().count(str2.lower()))

# проще
str1 = input('enter 1st string: ').lower()
str2 = input('enter 2nd string: ').lower()
print(str1.count(str2) or str2.count(str1))
