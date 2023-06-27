import pprint

number = 3
name = input('Enter a name: ')
e_mail = input('Enter an e-mail: ')
dict_info = {'name': name,
             'e-mail': e_mail
             }
dictionary = {number: dict_info for number in range(number)}
print(pprint.pprint(dictionary))
