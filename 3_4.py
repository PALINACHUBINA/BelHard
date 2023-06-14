positive = 0
negative = 0
for num in range(3):
    print('Введите', num + 1, 'число: ', end='')
    number = int(input())
    if number > 0:
        positive += 1
    else:
        negative += 1
print('Отрицательных чисел: ', negative)
print('Положительных чисел: ', positive)

