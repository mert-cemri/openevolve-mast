'''
This is the main module for the Morse code translator application. It sets up the CLI
and handles user interactions.
'''
import sys
from morse_code_translator import MorseCodeTranslator
def main():
    translator = MorseCodeTranslator()
    if len(sys.argv) < 3:
        print("Usage: python main.py <mode> <text>")
        print("<mode>: 'encode' to translate text to Morse, 'decode' to translate Morse to text")
        sys.exit(1)
    mode = sys.argv[1]
    text = ' '.join(sys.argv[2:])
    if mode == 'encode':
        result = translator.text_to_morse(text)
    elif mode == 'decode':
        result = translator.morse_to_text(text)
    else:
        print("Invalid mode. Use 'encode' or 'decode'.")
        sys.exit(1)
    print(result)
if __name__ == "__main__":
    main()