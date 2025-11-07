'''
This module contains the MorseCodeTranslator class which provides methods to translate
between English text and Morse code.
'''
class MorseCodeTranslator:
    def __init__(self):
        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
            '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
        }
        self.inverse_morse_dict = {v: k for k, v in self.morse_dict.items()}
    def text_to_morse(self, text):
        '''Converts English text to Morse code.'''
        return '   '.join(' '.join(self.morse_dict.get(char.upper(), '') for char in word) for word in text.split())
    def morse_to_text(self, morse):
        '''Converts Morse code to English text.'''
        return ' '.join(''.join(self.inverse_morse_dict.get(code, '') for code in word.split(' ')) for word in morse.split('   '))