'''
Main entry point for the language translation application.
Handles CLI mode.
'''
import sys
from translator import Translator
def cli_mode():
    translator = Translator()
    text = input("Enter the text to translate: ").strip()
    target_language = input("Enter the target language (e.g., en, fr): ").strip()
    if not text or not target_language:
        print("Error: Text and target language must be provided.")
        return
    translation = translator.translate(text, target_language)
    print(f"Translation: {translation}")
def main():
    cli_mode()
if __name__ == "__main__":
    main()