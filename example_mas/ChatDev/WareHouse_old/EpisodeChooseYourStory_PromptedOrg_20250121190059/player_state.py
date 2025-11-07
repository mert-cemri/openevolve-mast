'''
Manages the player's state, including relationships and items.
'''
class PlayerState:
    def __init__(self):
        self.state = {}
    def update_state(self, effects):
        for key, value in effects.items():
            if key in self.state:
                self.state[key] += value
            else:
                self.state[key] = value
    def get_state(self):
        return self.state