'''
Defines the Snake class, managing snake movement, growth, and collision detection.
'''
class Snake:
    def __init__(self):
        self.body = [(10, 10)]
        self.direction = 'RIGHT'
        self.grow_next_move = False
    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'UP':
            head_y -= 1
        elif self.direction == 'DOWN':
            head_y += 1
        elif self.direction == 'LEFT':
            head_x -= 1
        elif self.direction == 'RIGHT':
            head_x += 1
        new_head = (head_x, head_y)
        self.body.insert(0, new_head)
        if not self.grow_next_move:
            self.body.pop()
        else:
            self.grow_next_move = False
    def grow(self):
        self.grow_next_move = True
    def change_direction(self, direction):
        opposite_directions = {'UP':'DOWN', 'DOWN':'UP', 'LEFT':'RIGHT', 'RIGHT':'LEFT'}
        if direction != opposite_directions.get(self.direction):
            self.direction = direction
    def check_collision(self, width, height):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
            return True
        if self.body[0] in self.body[1:]:
            return True
        return False