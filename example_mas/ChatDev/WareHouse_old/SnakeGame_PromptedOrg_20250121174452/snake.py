'''
Snake class represents the snake, manages movement, growth, and collision detection.
'''
class Snake:
    def __init__(self, board):
        self.board = board
        self.body = [(5, 5), (5, 4), (5, 3)]
        self.direction = 'RIGHT'
        self.grow_flag = False
    @property
    def head(self):
        return self.body[0]
    def change_direction(self, new_direction):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction
    def move(self):
        x, y = self.head
        if self.direction == 'UP':
            y -= 1
        elif self.direction == 'DOWN':
            y += 1
        elif self.direction == 'LEFT':
            x -= 1
        elif self.direction == 'RIGHT':
            x += 1
        new_head = (x, y)
        self.body.insert(0, new_head)
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False
    def grow(self):
        self.grow_flag = True
    def check_collision(self):
        x, y = self.head
        if x < 0 or x >= self.board.width or y < 0 or y >= self.board.height:
            return True
        if self.head in self.body[1:]:
            return True
        return False