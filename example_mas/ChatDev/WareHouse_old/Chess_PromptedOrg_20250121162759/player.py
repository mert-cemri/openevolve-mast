'''
Module to represent a player in the chess game.
'''
class Player:
    def __init__(self, color):
        self.color = color
    def make_move(self):
        move = input("Enter your move (e.g., e2e4): ")
        return move