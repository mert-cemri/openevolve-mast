'''
Player module to manage player actions.
'''
class Player:
    def __init__(self, color):
        self.color = color
    def make_move(self):
        move = input("Enter your move: ")
        return move