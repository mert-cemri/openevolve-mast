'''
Main application file for the translation CLI client.
'''
import sys
from translator import translate
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <text> <target_language>")
        sys.exit(1)
    text = sys.argv[1]
    target_language = sys.argv[2]
    try:
        translated_text = translate(text, target_language)
        print("Translated text:", translated_text)
    except Exception as e:
        print("Translation Error:", str(e))
if __name__ == "__main__":
    main()