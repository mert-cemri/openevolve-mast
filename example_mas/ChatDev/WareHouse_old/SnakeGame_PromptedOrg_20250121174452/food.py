'''
Food class represents the food items on the board.
'''
import random
class Food:
    def __init__(self, board, snake):
        self.board = board
        self.snake = snake
        self.position = None
    def spawn(self):
        while True:
            x = random.randint(0, self.board.width - 1)
            y = random.randint(0, self.board.height - 1)
            if (x, y) not in self.snake.body:
                self.position = (x, y)
                break