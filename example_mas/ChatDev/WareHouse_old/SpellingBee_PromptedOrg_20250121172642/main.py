'''
This is the main module to run the Spelling Bee game, handle user input, and display feedback.
'''
from spelling_bee_game import SpellingBeeGame
def main():
    central_letter = 'e'
    surrounding_letters = ['a', 'b', 'c', 'd', 'f', 'g']
    game = SpellingBeeGame(central_letter, surrounding_letters)
    print("Welcome to the Spelling Bee Game!")
    print(f"Central Letter: {central_letter}")
    print(f"Surrounding Letters: {', '.join(surrounding_letters)}")
    while True:
        user_input = input("Enter a word (or 'exit' to quit): ").strip().lower()
        if user_input == 'exit':
            break
        success, feedback = game.add_word(user_input)
        print(feedback)
        print(game.get_feedback())
    print("Thanks for playing! Final Score:", game.score)
if __name__ == "__main__":
    main()