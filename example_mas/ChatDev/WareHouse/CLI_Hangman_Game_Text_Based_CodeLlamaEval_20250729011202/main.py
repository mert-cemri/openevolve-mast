import word
import guess
import display
import utils
def main():
    # Initialize the game state
    word = utils.get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    # Start the game loop
    while True:
        # Display the word with guessed letters filled in
        display.display_word(word, guessed_letters)
        # Get the user's guess
        guess = input("Guess a letter: ")
        # Check if the guess is correct
        if guess in word:
            # Add the guessed letter to the list of guessed letters
            guessed_letters.append(guess)
            # Check if the word has been guessed
            if word in guessed_letters:
                print("You guessed the word!")
                break
        else:
            # Increment the number of incorrect guesses
            incorrect_guesses += 1
            # Check if the user has run out of guesses
            if incorrect_guesses == 6:
                print("You have run out of guesses. The word was:", word)
                break
if __name__ == "__main__":
    main()