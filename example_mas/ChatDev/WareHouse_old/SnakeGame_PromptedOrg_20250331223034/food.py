'''
Defines the Food class, managing food generation and placement.
'''
import random
class Food:
    def __init__(self, width, height, snake_body):
        self.width = width
        self.height = height
        self.position = self.generate_position(snake_body)
    def generate_position(self, snake_body):
        while True:
            position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
            if position not in snake_body:
                return position