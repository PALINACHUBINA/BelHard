import mail as mail

info_dictionary = {123: {'name': 'Pavel', 'surname': 'Petrov',
                         'phone_number': '+375448534097',
                         'e-mail': 'pavel@gmail.com'},
                   234: {'name': 'Liza', 'surname': 'Peterson',
                         'phone_number': '+17026659811',
                         'e-mail': 'liza@gmail.com'},
                   345: {'name': 'Bob', 'surname': 'Pepper',
                         'phone_number': '+4746895234',
                         'e-mail': 'bob@gmail.com'},
                   456: {'name': 'Masha', 'surname': 'Ivanova',
                         'phone_number': '+375297893622',
                         'e-mail': 'masha@gmail.com'},
                   567: {'name': 'Scott', 'surname': 'Gray',
                         'phone_number': '+47429632200',
                         '': 'scott@gmail.com'},
                   678: {'name': 'Bruno', 'surname': 'Salinas',
                         'phone_number': '+17028891144',
                         'e-mail': 'bruno@gmaibrunol.com'},
                   789: {'name': 'Marry', 'surname': 'Haggen',
                         'phone_number': '+47467782234',
                         'e-mail': 'marry@gmail.com'},
                   890: {'name': 'Tommy', 'surname': 'Flower',
                         'phone_number': '+17023321894',
                         '': 'tommy@gmail.com'}
                   }

new_list = []
for person in info_dictionary.values():
    if person.get('e-mail'):
        continue
    new_list.append(person['name'])
print(new_list)


