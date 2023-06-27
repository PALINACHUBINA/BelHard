import pprint

number = int(input('Enter the lenght of the dictionaty: '))
names = [input('Enter a name: ') for _ in range(number)]
e_mails = [input('Enter an e-mail: ') for _ in range(number)]
dictionary = {i: {'name': names[i], 'e-mail': e_mails[i]} for i in range(number)}

print(pprint.pprint(dictionary))
