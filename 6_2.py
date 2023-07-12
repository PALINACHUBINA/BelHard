def message_encoding(text, data):
    """The function encoding the message according to Morse code."""
    new_message = []
    for symbol in message:
        if symbol in morse_dictionary:
            value = morse_dictionary.get(symbol)
            new_message.append(value)
    return new_message


message = input('Enter the text message in English for encoding: ').upper()
morse_dictionary = {'A': '.-', 'J': '.---', 'S': '...', 1: '.----',
                    'B': '-...', 'K': '-.-', 'T': '-', 2: '..---',
                    'C': '-.-.', 'L': '.-..', 'U': '..-', 3: '...--',
                    'D': '-..', 'M': '--', 'V': '...-', 4: '....-',
                    'E': '.', 'N': '-.', 'W': '.--', 5: '.....',
                    'F': '..-.', 'O': '---', 'X': '-..-', 6: '-....',
                    'G': '--.', 'P': '.--.', 'Y': '-.--', 7: '--...',
                    'H': '....', 'Q': '--.-', 'Z': '--..', 8: '---..',
                    'I': '..', 'R': '.-.', 0: '-----', 9: '----.'
                    }
message_Morse = message_encoding(message, morse_dictionary)
print('Encrypted message: ', ''.join(message_Morse))
