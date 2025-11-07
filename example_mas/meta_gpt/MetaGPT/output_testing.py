import random

def mastermind_game():
    # Define the possible colors or digits
    colors = ['1', '2', '3', '4', '5', '6']
    # Define the number of tries
    tries = 10
    # Generate a random sequence of 4 colors/digits
    code = random.sample(colors, 4)
    
    print("Welcome to Mastermind!")
    print("Try to guess the 4-digit code, using digits 1-6.")
    print("After each guess, you'll get feedback.")
    print("'+' means correct digit in the correct place.")
    print("'-' means correct digit but in the wrong place.")
    print("You have 10 tries. Good luck!\n")

    for attempt in range(tries):
        guess = input(f"Attempt {attempt + 1}/{tries}. Enter your guess: ")
        if len(guess) != 4 or not all(char in colors for char in guess):
            print("Invalid input. Make sure your guess is 4 digits long, using digits 1-6.")
            continue

        if guess == ''.join(code):
            print("Congratulations! You've guessed the code!")
            return

        feedback = ''
        temp_code = list(code)  # Temporary list to track matched digits
        for i, digit in enumerate(guess):
            if digit == code[i]:
                feedback += '+'
                temp_code[i] = None  # Mark as matched
            elif digit in temp_code:
                feedback += '-'
                temp_code[temp_code.index(digit)] = None  # Mark as matched

        print(f"Feedback: {feedback or 'No correct digits'}")

    print(f"Sorry, you've run out of tries. The code was {''.join(code)}.")

mastermind_game()

# correct = [ 0, 3, 4, 6, 7, 11, 13, 15, 17, 20, 27, 29]
# incorrect = [1, 2, 5, 8, 9, 10, 12, 14, 16, 18, 19, 21, 22, 23, 24, 25, 26, 28]