'''
Contains utility functions for the game.
'''
def position_to_coords(pos):
    # Convert board notation to screen coordinates
    row, col = pos
    return col * 100, row * 100
def coords_to_position(x, y):
    # Convert screen coordinates to board notation
    return y // 100, x // 100