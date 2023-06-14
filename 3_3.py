name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))
city = input('Введите Ваш город: ')
print('Меня зовут %s. Мне %d. Я живу в городе %s.' % (name, age, city))
print(f'Меня зовут {name}. Мне {age}. Я живу в городе {city}.')
print('Меня зовут {name}. Мне {age}. Я живу в городе {city}.'.format(
    name=name, age=age, city=city
))
