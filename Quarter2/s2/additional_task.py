# Вводится кол-во чисел N, далее сами числа. Найти ср. арфифм. всех положительных чисел
# с последней цифрой 7
#


n = int(input('enter N: '))
nums = []
target = []

for i in range(n):
    nums.append(int(input(f'enter {i+1} number: ')))
    if (nums[i] > 0) and (nums[i] % 10 == 7):
        target.append(nums[i])
if len(target) != 0:
    print(sum(target) / len(target))
else:
    print('no numbers with such conditions')
