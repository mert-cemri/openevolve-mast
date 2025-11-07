'''
Main file to run the Spelling Bee puzzle application.
'''
from game import SpellingBeeGame
from ui import display_welcome_message, get_user_input, display_feedback
def main():
    # Initialize the game with a central letter and surrounding letters
    central_letter = 'e'
    surrounding_letters = ['a', 'b', 'c', 'd', 'f', 'g']
    game = SpellingBeeGame(central_letter, surrounding_letters)
    display_welcome_message()
    while True:
        word = get_user_input()
        if word.lower() == 'exit':
            break
        if game.is_valid_word(word):
            score = game.calculate_score(word)
            game.add_word(word)
            display_feedback(word, score)
        else:
            print("Invalid word. Try again.")
if __name__ == "__main__":
    main()