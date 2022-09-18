import func_example as fe   # импортируем по имени файла + делаем алиас

fe.f('Import checked successfully')     # вызов с параметром
# без параметра - дефолтное значение, указанное в функции
fe.f()

print(fe.concatenation('q', 'w', 'w', 'r'))
