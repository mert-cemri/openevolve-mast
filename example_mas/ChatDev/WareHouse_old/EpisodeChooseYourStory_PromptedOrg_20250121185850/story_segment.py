'''
Represents a segment of the story.
'''
class StorySegment:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices
    def get_choices(self):
        return self.choices.keys()
    def get_next_segment(self, choice):
        return self.choices.get(choice, None)