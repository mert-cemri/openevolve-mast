'''
Defines the StorySegment class, representing a segment of the story.
'''
class StorySegment:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices
    def present(self):
        print(self.text)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")