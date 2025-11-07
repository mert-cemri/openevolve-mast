'''
This is the main module to run the CLI-based Morse Code Translator application.
'''
from morse_code_translator import MorseCodeTranslator
def main():
    '''Runs the CLI-based Morse Code Translator application.'''
    while True:
        choice = input("Choose an option: (1) Text to Morse (2) Morse to Text (3) Exit: ")
        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            print("Morse Code:", MorseCodeTranslator.text_to_morse(text))
        elif choice == '2':
            morse = input("Enter Morse code to convert to text: ")
            print("Text:", MorseCodeTranslator.morse_to_text(morse))
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()