'''
Segment module to represent individual word segments in the NYT Strands puzzle.
'''
class Segment:
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text