number_1 = int(input('Enter a first number: '))
print('Enter an action:\n1-multiplication,\n2-division,\n3-addition,\n4-subtraction: ', end='')
action = int(input(''))
number_2 = int(input('Enter a second number: '))
if action == 1:
    print(number_1 * number_2)
elif action == 2:
    print(round(number_1 / number_2, 2))
elif action == 3:
    print(number_1 * number_2)
elif action == 4:
    print(number_1 - number_2)
else:
    print('Input error. There is no such action!')
