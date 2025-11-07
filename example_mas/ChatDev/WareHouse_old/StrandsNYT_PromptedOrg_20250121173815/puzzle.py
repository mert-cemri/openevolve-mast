'''
Puzzle module to represent the NYT Strands puzzle and validate connections.
'''
from segment import Segment
class Puzzle:
    def __init__(self, segments):
        self.segments = [Segment(s) for s in segments]
        self.connected_segments = []
    def connect_segments(self, indices):
        # Attempt to connect the selected segments
        selected_segments = [self.segments[i] for i in indices]
        word = ''.join(segment.text for segment in selected_segments)
        if self.is_valid_word(word):
            self.connected_segments.append(word)
            return True
        return False
    def is_valid_word(self, word):
        # Check if the formed word is valid (for simplicity, assume any non-empty string is valid)
        return len(word) > 0
    def is_solved(self):
        # Check if all segments are used in valid connections
        used_segments_set = set(''.join(self.connected_segments))
        original_segments_set = set(segment.text for segment in self.segments)
        return used_segments_set == original_segments_set