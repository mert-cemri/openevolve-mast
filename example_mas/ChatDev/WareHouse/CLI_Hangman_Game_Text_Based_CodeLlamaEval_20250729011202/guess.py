def check_guess(word, guess):
    # Check if the guess is in the word
    if guess in word:
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)
        # Check if the word has been guessed
        if word in guessed_letters:
            print("You guessed the word!")
            return True
    else:
        # Increment the number of incorrect guesses
        incorrect_guesses += 1
        # Check if the user has run out of guesses
        if incorrect_guesses == 6:
            print("You have run out of guesses. The word was:", word)
            return False