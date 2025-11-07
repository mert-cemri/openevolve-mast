'''
Player class to represent a player in the chess game.
'''
class Player:
    def __init__(self, color):
        self.color = color
    def get_move(self):
        move = input(f"{self.color} player, enter your move: ")
        return move