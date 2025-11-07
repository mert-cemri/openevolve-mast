'''
Main application file for the Typing Speed Tester. Manages user interactions via CLI.
'''
from text_generator import get_random_paragraph
from typing_logic import TypingTest
def main():
    paragraph = get_random_paragraph()
    typing_test = TypingTest(paragraph)
    print("Typing Speed Tester")
    print("Type the following paragraph as fast and accurately as you can:")
    print(paragraph)
    input("Press Enter to start...")
    typing_test.start()
    typed_text = input("Start typing here:\n")
    typing_test.update_typed_text(typed_text)
    if typing_test.is_complete():
        wpm, accuracy = typing_test.calculate_results()
        print(f"\nResults:\nWPM: {wpm}\nAccuracy: {accuracy}%")
    else:
        print("\nTyping test was not completed correctly.")
if __name__ == "__main__":
    main()