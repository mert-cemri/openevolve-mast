'''
Snake module to manage the snake's behavior.
'''
class Snake:
    def __init__(self, block_size):
        self.block_size = block_size
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'RIGHT'
        self.grow_flag = False
    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'UP':
            head_y -= self.block_size
        elif self.direction == 'DOWN':
            head_y += self.block_size
        elif self.direction == 'LEFT':
            head_x -= self.block_size
        elif self.direction == 'RIGHT':
            head_x += self.block_size
        new_head = (head_x, head_y)
        self.body.insert(0, new_head)
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False
    def change_direction(self, direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if direction != opposite_directions.get(self.direction) and direction != self.direction:
            self.direction = direction
    def grow(self):
        self.grow_flag = True
    def check_collision(self, width, height):
        head_x, head_y = self.body[0]
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
            return True
        if len(self.body) != len(set(self.body)):
            return True
        return False
    def eat_food(self, food_position):
        return self.body[0] == food_position