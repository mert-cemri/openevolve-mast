'''
Represents a single word segment in the game.
'''
class Segment:
    def __init__(self, text):
        self.text = text
        self.is_selected = False