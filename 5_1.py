number = int(input('Enter the number of output numbers: '))
multiplicity = int(input('Enter multiplicity: '))
start_number = int(input('Enter the starting number: '))
counter = 0
for i in range(number):
    counter = start_number
    start_number += multiplicity
    print(counter, end='\t')
