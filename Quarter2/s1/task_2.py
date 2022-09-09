# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, j, k, not(i or j or k) == (not i and not j and not k))
