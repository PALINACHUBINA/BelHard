numbers_sum = 0
for num in range(3):
    print('Введите', num + 1, 'число: ', end='')
    number = int(input())
    numbers_sum += number
print('Среднее арифметическое всех чисел: ', round(numbers_sum / 3, 3))