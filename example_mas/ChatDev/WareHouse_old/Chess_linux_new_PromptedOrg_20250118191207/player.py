'''
Represents a player in the chess game.
'''
class Player:
    def __init__(self, color):
        self.color = color
    def make_move(self):
        move_input = input(f"{self.color} player, enter your move: ")
        return self.parse_move(move_input)
    def parse_move(self, input_str):
        # Simplified parsing logic
        start = (int(input_str[1]) - 1, ord(input_str[0]) - ord('a'))
        end = (int(input_str[4]) - 1, ord(input_str[3]) - ord('a'))
        return start, end