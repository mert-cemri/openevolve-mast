'''
This is the main file for the Wordle game. It initializes the game and handles user interaction.
'''
import random
from wordle_game import WordleGame
def get_daily_word():
    '''
    Retrieve the daily word. This function randomly selects a word from a predefined list.
    '''
    words = ["apple", "grape", "peach", "berry", "melon"]
    return random.choice(words)
def main():
    '''
    Main function to start the Wordle game.
    '''
    daily_word = get_daily_word()
    game = WordleGame(daily_word)
    print("Welcome to Wordle! Guess the 5-letter word.")
    for attempt in range(6):
        guess = input(f"Attempt {attempt + 1}/6: ").strip().lower()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        feedback, is_correct = game.evaluate_guess(guess)
        game.display_feedback(feedback)
        if is_correct:
            print("Congratulations! You've guessed the word correctly.")
            break
    else:
        print(f"Sorry, you've used all attempts. The word was: {daily_word}")
if __name__ == "__main__":
    main()