'''
Map class to represent the game map.
'''
import random
from position import Position
from monster import Monster
from treasure_chest import TreasureChest
class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.generate_map()
        self.start_position = Position(0, 0)  # Example starting position
        self.door_position = Position(width - 1, height - 1)  # Example door position
    def generate_map(self):
        grid = [['.' for _ in range(self.width)] for _ in range(self.height)]
        # Ensure a path from start to door using DFS
        self.create_path(grid, self.start_position, self.door_position)
        # Place walls randomly but not on the path
        for y in range(self.height):
            for x in range(self.width):
                if grid[y][x] == '.' and random.random() < 0.2:
                    grid[y][x] = '#'
        # Place monsters and treasure chests randomly
        for _ in range(10):  # Example: place 10 monsters
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if grid[y][x] == '.':
                grid[y][x] = Monster(random.randint(10, 50))  # Random monster HP
        for _ in range(5):  # Example: place 5 treasure chests
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if grid[y][x] == '.':
                grid[y][x] = TreasureChest()
        return grid
    def create_path(self, grid, start, end):
        # Simple DFS to create a path
        stack = [start]
        visited = set()
        while stack:
            position = stack.pop()
            if position == end:
                return True
            if position in visited:
                continue
            visited.add(position)
            grid[position.y][position.x] = '.'
            for direction in ['W', 'S', 'A', 'D']:
                new_position = position.move(direction)
                if self.is_within_bounds(new_position) and new_position not in visited:
                    stack.append(new_position)
        return False
    def is_within_bounds(self, position):
        return 0 <= position.x < self.width and 0 <= position.y < self.height
    def display(self, player_position):
        for y in range(self.height):
            for x in range(self.width):
                if Position(x, y) == player_position:
                    print('P', end=' ')
                elif Position(x, y) == self.door_position:
                    print('D', end=' ')
                else:
                    print(self.grid[y][x], end=' ')
            print()
    def is_door(self, position):
        return position == self.door_position
    def is_monster(self, position):
        return isinstance(self.grid[position.y][position.x], Monster)
    def get_monster(self, position):
        return self.grid[position.y][position.x]
    def is_treasure(self, position):
        return isinstance(self.grid[position.y][position.x], TreasureChest)
    def get_treasure(self, position):
        return self.grid[position.y][position.x]
    def is_valid_move(self, position):
        # Check if the position is within the map boundaries
        if 0 <= position.x < self.width and 0 <= position.y < self.height:
            # Check if the position is not a wall
            return self.grid[position.y][position.x] != '#'
        return False