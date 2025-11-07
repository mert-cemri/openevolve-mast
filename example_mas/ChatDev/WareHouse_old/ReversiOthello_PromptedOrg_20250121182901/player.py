'''
Player module to manage player actions in the Reversi game.
'''
class Player:
    def __init__(self, color):
        self.color = color
    def make_move(self, valid_moves):
        # Display valid moves to the player
        print("Valid moves:", valid_moves)
        # Use a separate method to get the player's move
        return self.get_move_from_input(valid_moves)
    def get_move_from_input(self, valid_moves):
        # Abstracted method for getting player input
        while True:
            try:
                move_index = int(input(f"Player {self.color}, select a move (0-{len(valid_moves)-1}): "))
                if 0 <= move_index < len(valid_moves):
                    return valid_moves[move_index]
                else:
                    print("Invalid selection. Please choose a valid move index.")
            except ValueError:
                print("Invalid input. Please enter a number.")