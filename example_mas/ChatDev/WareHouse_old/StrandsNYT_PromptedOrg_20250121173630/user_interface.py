'''
UserInterface module to manage user interactions.
'''
class UserInterface:
    def __init__(self, puzzle):
        '''
        Initialize the user interface with the puzzle.
        '''
        self.puzzle = puzzle
    def start_game(self):
        '''
        Start the game and manage user interactions.
        '''
        print("Welcome to the NYT Strands Puzzle!")
        while True:
            print("Available segments:")
            for i, segment in enumerate(self.puzzle.segments):
                print(f"{i}: {segment.text}")
            try:
                indices_input = input("Enter indices of segments to connect (comma-separated): ").strip()
                if not indices_input:
                    raise ValueError("Input cannot be empty.")
                indices = list(map(int, indices_input.split(',')))
                if any(i < 0 or i >= len(self.puzzle.segments) for i in indices):
                    raise ValueError("Index out of range.")
                word = self.puzzle.connect_segments(indices)
                print(f"Formed word: {word}")
                if self.puzzle.is_valid_solution(word):
                    print("Congratulations! You formed a valid word.")
                else:
                    print("Try again.")
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter valid indices.")
                continue
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() != 'y':
                break