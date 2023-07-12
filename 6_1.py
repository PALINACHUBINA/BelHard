number = int(input('Enter an integer in decimal notation: '))


def convert_number(number):
    """The function convert a decimal number to binary and vice verse."""
    binary_form = bin(number)
    return binary_form


result = convert_number(number)
decimal_form = eval(result)
print('A binary number {0} corresponds to a decimal number {1}.'.format(result, decimal_form))
