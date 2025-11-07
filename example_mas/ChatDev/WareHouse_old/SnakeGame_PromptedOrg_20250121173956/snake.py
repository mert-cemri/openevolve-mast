'''
Represents the snake, including its position, direction, and methods to move and grow.
'''
class Snake:
    def __init__(self, board):
        self.board = board
        self.body = [(board.width // 2, board.height // 2)]
        self.direction = (0, 1)  # Start moving down
    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)
        self.body.pop()
    def grow(self):
        self.body.append(self.body[-1])
    def has_collided_with_wall(self):
        head = self.body[0]
        return not self.board.is_within_bounds(head)
    def has_collided_with_self(self):
        head = self.body[0]
        return head in self.body[1:]
    def has_eaten_food(self, food):
        return self.body[0] == food.position
    def change_direction(self, new_direction):
        # Prevent the snake from reversing into itself
        opposite_direction = (-self.direction[0], -self.direction[1])
        if new_direction != opposite_direction:
            self.direction = new_direction