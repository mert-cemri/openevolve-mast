'''
Food class to represent the food items on the board.
'''
import random
class Food:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.position = (0, 0)
        self.spawn([])
    def spawn(self, snake_body):
        while True:
            x = random.randint(0, self.board_width - 1)
            y = random.randint(0, self.board_height - 1)
            self.position = (x, y)
            if self.position not in snake_body:
                break