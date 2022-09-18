
colors = ['red', 'green', 'blue']
# данные дописываются в конец файла. логирование(?)
data = open('text.txt', 'w')
data.writelines(colors)     # без разделителей
data.write('\n')
data.write('NEWLINE 1\n')   # write не сработает со списками
data.write('NEWLINE 2\n')
data.close()

with open('text.txt', 'a') as data:
    data.write('appended line 1')   # разделение через пробел
    data.write('appended line 2')

path = 'text.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()


exit()  # дальнейший код не будет выполнен

while True:
    print('Oops')
