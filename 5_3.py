number = int(input('Enter a number: '))
counter = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        counter += 1
        print(num, end='\t')
        if counter % 5 == 0:
            print(end='\n')
