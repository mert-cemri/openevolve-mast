'''
User interface functions for the Spelling Bee puzzle.
'''
def display_welcome_message():
    print("Welcome to the Spelling Bee Puzzle!")
    print("Form words using the central letter and surrounding letters.")
    print("Type 'exit' to quit the game.")
def get_user_input():
    return input("Enter a word: ")
def display_feedback(word, score):
    print(f"Great! '{word}' is worth {score} points.")