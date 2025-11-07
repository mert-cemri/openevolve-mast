'''
Represents the food items on the board, including their position and methods to randomly place them on the board.
'''
import random
class Food:
    def __init__(self, board):
        self.board = board
        self.position = self.random_position()
    def random_position(self):
        return (random.randint(0, self.board.width - 1), random.randint(0, self.board.height - 1))
    def reposition(self, snake):
        while True:
            new_position = self.random_position()
            if new_position not in snake.body:
                self.position = new_position
                break