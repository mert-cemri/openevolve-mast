'''
Contains the Tetromino class representing Tetris shapes.
'''
class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.rotation = 0
        self.x = 0
        self.y = 0
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)
    def get_cells(self, dx=0, dy=0):
        cells = []
        for i in self.shape[self.rotation]:
            x = (i % 2) + self.x + dx
            y = (i // 2) + self.y + dy
            cells.append((x, y))
        return cells