'''
This is a simple command-line Wordle game implemented in Python. The player has 6 attempts to guess a daily 5-letter word. Feedback is provided after each guess, indicating correct letters in the correct position (green), correct letters in the wrong position (yellow), and incorrect letters (grey).
'''
import random
def get_daily_word():
    '''
    Retrieve or generate the daily word. For simplicity, we use a fixed list of words.
    '''
    words = ["apple", "grape", "peach", "berry", "melon"]
    return random.choice(words)
def get_user_guess():
    '''
    Get a valid 5-letter guess from the user.
    '''
    while True:
        guess = input("Enter your 5-letter guess: ").lower()
        if len(guess) == 5 and guess.isalpha():
            return guess
        print("Invalid input. Please enter a 5-letter word.")
def evaluate_guess(guess, daily_word):
    '''
    Evaluate the user's guess and return feedback.
    '''
    feedback = []
    for i in range(5):
        if guess[i] == daily_word[i]:
            feedback.append('green')
        elif guess[i] in daily_word:
            feedback.append('yellow')
        else:
            feedback.append('grey')
    return feedback
def display_feedback(guess, feedback):
    '''
    Display the feedback for the user's guess.
    '''
    feedback_display = ""
    for i in range(5):
        if feedback[i] == 'green':
            feedback_display += f"\033[92m{guess[i]}\033[0m "  # Green
        elif feedback[i] == 'yellow':
            feedback_display += f"\033[93m{guess[i]}\033[0m "  # Yellow
        else:
            feedback_display += f"\033[90m{guess[i]}\033[0m "  # Grey
    print(feedback_display)
def play_game():
    '''
    Manage the game flow, including attempts and win/lose conditions.
    '''
    daily_word = get_daily_word()
    attempts = 6
    print("Welcome to Wordle! You have 6 attempts to guess the 5-letter word.")
    for attempt in range(attempts):
        guess = get_user_guess()
        feedback = evaluate_guess(guess, daily_word)
        display_feedback(guess, feedback)
        if guess == daily_word:
            print("Congratulations! You've guessed the word correctly!")
            return
    print(f"Sorry, you've used all attempts. The word was: {daily_word}")
def main():
    '''
    Main function to run the game loop.
    '''
    play_game()
if __name__ == "__main__":
    main()