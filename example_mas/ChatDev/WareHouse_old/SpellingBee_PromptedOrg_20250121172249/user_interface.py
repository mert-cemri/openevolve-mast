'''
DOCSTRING: Manages user interaction, displaying messages and receiving input.
'''
class UserInterface:
    def display_welcome_message(self, central_letter, surrounding_letters):
        print(f"Welcome to the Spelling Bee Game!")
        print(f"Central Letter: {central_letter}")
        print(f"Surrounding Letters: {', '.join(surrounding_letters)}")
        print("Type 'exit' to quit the game.")
    def get_user_input(self):
        return input("Enter a word: ").strip().lower()
    def display_score(self, score):
        print(f"Valid word! You scored {score} points.")
    def display_invalid_word_message(self):
        print("Invalid word. Please try again.")