'''
Food module to manage the food's behavior.
'''
import random
class Food:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.position = (0, 0)
        self.spawn([])
    def spawn(self, snake_body):
        while True:
            x = random.randint(0, (self.width // self.block_size) - 1) * self.block_size
            y = random.randint(0, (self.height // self.block_size) - 1) * self.block_size
            self.position = (x, y)
            if self.position not in snake_body:
                break