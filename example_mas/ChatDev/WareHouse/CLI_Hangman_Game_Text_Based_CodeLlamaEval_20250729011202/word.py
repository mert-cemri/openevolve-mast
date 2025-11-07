import utils
def get_random_word():
    # Generate a random word
    word = utils.get_random_word()
    # Return the word
    return word
def get_word_with_guessed_letters(word, guessed_letters):
    # Create a list of the word's letters
    word_letters = list(word)
    # Replace the letters in the word with the guessed letters
    for i in range(len(word_letters)):
        if word_letters[i] in guessed_letters:
            word_letters[i] = guessed_letters[i]
    # Return the word with the guessed letters filled in
    return "".join(word_letters)