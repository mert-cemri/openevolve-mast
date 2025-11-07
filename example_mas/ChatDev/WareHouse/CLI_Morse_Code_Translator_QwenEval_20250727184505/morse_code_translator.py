'''
This module contains the MorseCodeTranslator class which handles the translation between English and Morse code.
'''
class MorseCodeTranslator:
    def __init__(self):
        self.morse_code_dict = load_morse_code_dict()
    def translate_to_morse(self, text):
        '''
        Translates English text to Morse code.
        Unknown characters are replaced with '?'.
        '''
        text = text.upper()
        morse_code = []
        for char in text:
            morse_code.append(self.morse_code_dict.get(char, '?'))  # Unknown character
        return ' '.join(morse_code)
    def translate_to_english(self, morse_code):
        '''
        Translates Morse code to English text.
        Unknown Morse code sequences are replaced with '?'.
        '''
        morse_code = morse_code.split()
        english_text = []
        reverse_morse_code_dict = {v: k for k, v in self.morse_code_dict.items()}
        for code in morse_code:
            english_text.append(reverse_morse_code_dict.get(code, '?'))  # Unknown Morse code
        return ''.join(english_text)
def load_morse_code_dict():
    '''
    Loads the Morse code dictionary.
    '''
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
    }
    return morse_code_dict