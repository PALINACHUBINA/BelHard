text = input('Enter the text: ')
dictionary = {letter: text.count(letter) for letter in text}
print(dictionary)

