'''
Game module to manage the game state and user interactions for the NYT Strands puzzle.
'''
from puzzle import Puzzle
class Game:
    def __init__(self):
        # Initialize the puzzle with predefined segments
        self.puzzle = Puzzle([
            "con", "nect", "ion", "nect", "ed", "word", "seg", "ments"
        ])
    def start(self):
        print("Welcome to the NYT Strands Puzzle!")
        while not self.puzzle.is_solved():
            self.display_segments()
            user_input = input("Select segments to connect (comma-separated indices): ")
            indices = [int(i.strip()) for i in user_input.split(",")]
            if self.puzzle.connect_segments(indices):
                print("Correct connection!")
            else:
                print("Invalid connection, try again.")
        print("Congratulations! You've solved the puzzle.")
    def display_segments(self):
        print("Available segments:")
        for i, segment in enumerate(self.puzzle.segments):
            print(f"{i}: {segment}")