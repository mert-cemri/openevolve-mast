'''
This module contains the CLIInterface class which handles the command-line interface for the Morse code translator.
'''
from morse_code_translator import MorseCodeTranslator
class CLIInterface:
    def __init__(self):
        self.translator = MorseCodeTranslator()
    def run(self):
        '''
        Runs the Morse Code Translator CLI.
        '''
        print("Welcome to the Morse Code Translator CLI!")
        print("Type 'exit' to quit.")
        while True:
            user_input = input("Enter text to translate to Morse code or Morse code to translate to text: ").strip()
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            if not user_input:
                print("Input cannot be empty. Please try again.")
                continue
            if self.is_morse_code(user_input):
                result = self.translator.translate_to_english(user_input)
                print(f"Translated English text: {result}")
            else:
                result = self.translator.translate_to_morse(user_input)
                print(f"Translated Morse code: {result}")
    def is_morse_code(self, input_text):
        '''
        Determines if the input text is Morse code.
        Morse code contains only '.', '-', ' ', and '/'.
        '''
        valid_morse_chars = {'.', '-', ' ', '/'}
        return all(char in valid_morse_chars for char in input_text)
if __name__ == "__main__":
    cli = CLIInterface()
    cli.run()