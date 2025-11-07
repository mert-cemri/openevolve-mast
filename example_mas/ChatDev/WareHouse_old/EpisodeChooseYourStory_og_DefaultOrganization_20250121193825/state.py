'''
Defines the GameState class to track game variables.
'''
class GameState:
    def __init__(self):
        self.variables = {}
    def update(self, variable, value):
        if variable in self.variables:
            self.variables[variable] += value
        else:
            self.variables[variable] = value