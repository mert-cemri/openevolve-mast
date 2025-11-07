'''
Manages the clues for the crossword puzzle.
'''
class ClueManager:
    def __init__(self):
        self.across_clues = {
            1: "Greeting",
            2: "Planet",
            3: "Programming language",
            4: "Pleasant",
            5: "Person who writes code"
        }
        self.down_clues = {
            1: "Opposite of goodbye",
            2: "Earth",
            3: "Python's creator",
            4: "Opposite of mean",
            5: "Software developer"
        }
        self.start_positions = {
            'across': {
                1: (0, 0),
                2: (1, 0),
                3: (2, 0),
                4: (3, 0),
                5: (4, 0)
            },
            'down': {
                1: (0, 0),
                2: (0, 1),
                3: (0, 2),
                4: (0, 3),
                5: (0, 4)
            }
        }
    def get_clue(self, number, direction):
        if direction.lower() == 'across':
            return self.across_clues.get(number, "No clue available")
        elif direction.lower() == 'down':
            return self.down_clues.get(number, "No clue available")
        else:
            return "Invalid direction"
    def get_start_position(self, number, direction):
        return self.start_positions[direction].get(number, (None, None))