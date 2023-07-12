dict_cities = {'Norway': 'Oslo, Stavanger, Bergen',
               'Belarus': 'Minsk, Grodno, Brest',
               'Germany': 'Berlin, Dresden, Hamburg',
               'Italy': 'Milan, Rome, Palermo',
               'USA': 'Las Vegas, Boston, Huston',
               'Spain': 'Barcelona, Toledo, Madrid',
               'England': 'London, Manchester, Liverpool',
               'Netherlands': 'Amsterdam, Rotterdam, Oss',
               'Canada': 'Toronto, Montreal, Vancouver'
               }

desired_city = input('Enter the city which you want to find: ').title()


def found_city(city) -> str:
    """
    The function finds the city.
    :param city: str
    :return: s
    """
    for key, value in dict_cities.items():
        if city in value:
            return key


country = found_city(desired_city)
if country:
    print('The city of {city} is located in {country}.'.format(city=desired_city, country=country))
else:
    print('There is no city in the list which you are looking for.')
