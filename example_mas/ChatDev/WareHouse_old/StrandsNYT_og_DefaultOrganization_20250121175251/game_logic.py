'''
Game logic for the NYT Strands puzzle game.
'''
class GameLogic:
    def __init__(self):
        self.valid_phrases = ["hello world", "python code", "open source"]
    def load_segments(self):
        # This is a simple example; in a real game, this could be randomized or loaded from a file
        return [WordSegment("hello"), WordSegment("world"), WordSegment("python"), WordSegment("code"), WordSegment("open"), WordSegment("source")]
    def validate_solution(self, selected_segments):
        selected_text = " ".join([seg.get_text() for seg in selected_segments])
        return selected_text in self.valid_phrases