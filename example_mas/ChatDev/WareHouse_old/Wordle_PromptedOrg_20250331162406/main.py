'''
main.py
This module contains the main function to run the Wordle game from the terminal.
'''
from wordle_game import WordleGame
def main():
    '''
    Runs the Wordle game, allowing the player to guess the daily word.
    '''
    # Example word list
    word_list = ['apple', 'berry', 'charm', 'delta', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']
    game = WordleGame(word_list)
    attempts = 0
    print("Welcome to Wordle! Guess the 5-letter word.")
    while attempts < game.max_attempts:
        guess = input(f"Attempt {attempts + 1}/{game.max_attempts}: ").strip().lower()
        if len(guess) != 5 or not game.is_valid_word(guess):
            print("Invalid word. Please enter a valid 5-letter word.")
            continue
        feedback = game.check_guess(guess)
        print("Feedback:", feedback)
        if all(color == 'green' for color in feedback):
            print("Congratulations! You've guessed the word correctly.")
            break
        attempts += 1
    if attempts == game.max_attempts:
        print(f"Sorry, you've used all attempts. The word was: {game.get_daily_word()}")
if __name__ == "__main__":
    main()