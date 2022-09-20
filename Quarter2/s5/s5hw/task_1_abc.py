# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def get_line_from_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        return file.readline()


# def abv_excluder(s):
#     s = s.split()
#     tmp = []
#     for word in s:
#         if 'абв' in word:
#             continue
#         else:
#             tmp.append(word)
#     return ' '.join(tmp)


path = './text.txt'
in_text = get_line_from_file(path)

s = filter(lambda x: 'абв' not in x, in_text.split())
print(in_text)
print(' '.join(s))
