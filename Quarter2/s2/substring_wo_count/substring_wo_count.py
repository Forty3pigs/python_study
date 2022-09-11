str1 = input('1st: ')  # greater
str2 = input('2nd:')
# нужна проверка на пустые строки

i = 0
counter_in = 0
len_str1 = len(str1)
len_str2 = len(str2)

if str1 == str2:
    print(f'"{str1}" equal "{str2}"')
else:
    i = 0

    if len_str2 > len_str1:
        str1, str2 = str2, str1

    if len_str2 == 1:
        for j in str1:
            if j == str2:
                counter_in += 1
    else:

        while (i < len_str1):

            if (str1[i] == str2[0]) and (len_str2 > 1):
                j = 1
                i += 1

                while((i < (len_str1)) and (j < len_str2) and (str2[j] == str1[i])):

                    if j == len_str2 - 1:
                        counter_in += 1
                        break
                    else:
                        j += 1
                        i += 1

            i += 1
print(f'quantity: {counter_in}')
