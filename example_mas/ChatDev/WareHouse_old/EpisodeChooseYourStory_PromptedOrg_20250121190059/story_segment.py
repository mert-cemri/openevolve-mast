'''
Defines the StorySegment and Choice classes for the storytelling game.
'''
class Choice:
    def __init__(self, description, next_segment_id, effects):
        self.description = description
        self.next_segment_id = next_segment_id
        self.effects = effects
class StorySegment:
    def __init__(self, narrative, choices):
        self.narrative = narrative
        self.choices = choices
    def display(self):
        print(self.narrative)
    def get_choices(self):
        return self.choices