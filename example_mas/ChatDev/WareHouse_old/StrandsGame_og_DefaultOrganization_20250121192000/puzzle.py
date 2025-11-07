'''
Puzzle logic for the Strands word-segmentation puzzle. Handles strand verification and completion checking.
'''
class StrandsPuzzle:
    def __init__(self):
        # Example strands and solution
        self.strands = ["hel", "lo", "wor", "ld"]
        self.solution = "hello world"
    def get_strands(self):
        return self.strands
    def check_solution(self, user_input):
        # Check if the user's input matches the solution
        return user_input.strip().lower() == self.solution.replace(" ", "").lower()