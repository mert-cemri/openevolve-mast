'''
Game logic for managing word segments and checking solutions.
'''
from segment import Segment
class Game:
    def __init__(self):
        self.segments = []
        self.load_segments()
        self.selected_segments = []
    def load_segments(self):
        # Load word segments (this could be from a file or predefined list)
        words = ["py", "thon", "pro", "gram", "ming", "code"]
        self.segments = [Segment(text) for text in words]
    def check_solution(self):
        # Check if the selected segments form a valid word or phrase
        solution = "".join(segment.text for segment in self.selected_segments)
        valid_solutions = ["python", "programming", "code"]
        return solution in valid_solutions
    def reset_game(self):
        # Reset the game state
        self.selected_segments.clear()
        for segment in self.segments:
            segment.is_selected = False