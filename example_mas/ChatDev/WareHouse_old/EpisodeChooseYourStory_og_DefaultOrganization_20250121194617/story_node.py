'''
Defines the StoryNode class representing a segment of the story.
'''
class StoryNode:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices
    def get_choices(self):
        return self.choices