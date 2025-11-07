'''
This is the main file that initializes the game and starts the game loop.
'''
from game import Game
from user_interface import UserInterface
def main():
    # Initialize the game with words and categories
    words = [
        "apple", "banana", "cherry", "date",
        "carrot", "broccoli", "spinach", "lettuce",
        "dog", "cat", "hamster", "rabbit",
        "red", "blue", "green", "yellow"
    ]
    categories = {
        "Fruits": ["apple", "banana", "cherry", "date"],
        "Vegetables": ["carrot", "broccoli", "spinach", "lettuce"],
        "Animals": ["dog", "cat", "hamster", "rabbit"],
        "Colors": ["red", "blue", "green", "yellow"]
    }
    game = Game(words, categories)
    ui = UserInterface()
    # Start the game loop
    game.play(ui)
if __name__ == "__main__":
    main()