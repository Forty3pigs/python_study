# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

text1 = 'bbbbwwbbbbbwwwbbbbwbwwww'
text2 = 'bbbbwwbbbbbwwwbbbbwbwwwwb'
text3 = 'bwbwwwwwbbbb'

coded1 = '4b2w5b3w4bwb4w'
coded2 = '4b2w5b3w4bwb4w1b'
coded3 = 'bwb5w4b'


def cod(s):
    icount = 1
    output = ''
    l = len(s)
    for i in range(1, l):
        if s[i] == s[i-1]:
            icount += 1
        else:
            if icount == 1:
                output += s[i-1]
            else:
                output += str(icount) + s[i-1]
                icount = 1
    if icount == 1:
        output += output[-1]
    else:
        output += str(icount) + s[-1]
    return output


def dec(s):
    output = ''
    mult = 1
    l = len(s)
    for i in range(l):
        if s[i].isdigit():
            mult = int(s[i])
        else:
            if mult > 1:
                output += mult * s[i]
                mult = 1
            else:
                output += s[i]
    return output


print(cod(text1))
print(cod(text2))
print(cod(text3))

print(dec(coded1))
print(dec(coded2))
print(dec(coded3))
