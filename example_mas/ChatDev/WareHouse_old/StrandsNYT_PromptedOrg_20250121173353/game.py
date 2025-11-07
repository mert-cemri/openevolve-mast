'''
Game class handles the game logic, including user interactions and confirmations.
'''
from puzzle import Puzzle
class Game:
    def __init__(self, segments):
        '''
        Initialize the game with a list of word segments.
        :param segments: A list of strings representing word segments.
        '''
        self.puzzle = Puzzle(segments)
    def play(self):
        '''
        Start the game loop, allowing the user to make selections and receive confirmations.
        '''
        print("Welcome to the NYT Strands Puzzle!")
        while True:
            print("Available segments:")
            for i, segment in enumerate(self.puzzle.segments):
                print(f"{i}: {segment}")
            try:
                choice1 = int(input("Select the first segment index: "))
                choice2 = int(input("Select the second segment index: "))
                if self.puzzle.is_valid_connection(self.puzzle.segments[choice1], self.puzzle.segments[choice2]):
                    print("Correct connection!")
                else:
                    print("Invalid connection. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid indices.")