'''
Defines the NarrativeSegment and Choice classes for the storytelling game.
'''
class NarrativeSegment:
    def __init__(self, text, choices):
        self.text = text
        self.choices = choices
    def display(self):
        return self.text, self.choices
class Choice:
    def __init__(self, text, next_segment, effects):
        self.text = text
        self.next_segment = next_segment
        self.effects = effects
    def apply_effects(self, state):
        for variable, value in self.effects.items():
            state.update(variable, value)