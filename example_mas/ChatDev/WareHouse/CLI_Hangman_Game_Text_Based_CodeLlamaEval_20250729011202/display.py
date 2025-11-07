def display_word(word, guessed_letters):
    # Create a list of the word's letters
    word_letters = list(word)
    # Replace the letters in the word with the guessed letters
    for i in range(len(word_letters)):
        if word_letters[i] in guessed_letters:
            word_letters[i] = guessed_letters[i]
    # Display the word with the guessed letters filled in
    print(" ".join(word_letters))