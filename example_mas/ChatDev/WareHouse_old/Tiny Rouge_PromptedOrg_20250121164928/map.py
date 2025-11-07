'''
Map class to generate and manage the game map.
'''
import random
from monster import Monster
from treasure_chest import TreasureChest
from door import Door
from utils import random_position
class Map:
    def __init__(self):
        self.size = 80
        self.grid = self.generate_map()
        self.start_position = (0, 0)  # Example start position
        self.door_position = (self.size - 1, self.size - 1)  # Example door position
    def generate_map(self):
        grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        # Ensure at least one path from start to door
        self.create_path(grid, self.start_position, self.door_position)
        # Add walls, monsters, and treasure chests
        self.add_elements(grid)
        return grid
    def create_path(self, grid, start, end):
        # Implement a simple path creation using DFS
        stack = [start]
        visited = set()
        while stack:
            current = stack.pop()
            if current == end:
                break
            if current not in visited:
                visited.add(current)
                y, x = current
                grid[y][x] = ' '  # Mark path
                neighbors = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
                random.shuffle(neighbors)
                for ny, nx in neighbors:
                    if 0 <= ny < self.size and 0 <= nx < self.size and (ny, nx) not in visited:
                        stack.append((ny, nx))
    def add_elements(self, grid):
        # Add walls, monsters, and treasure chests randomly
        for _ in range(int(self.size * self.size * 0.1)):  # 10% walls
            y, x = random_position(self.size)
            if grid[y][x] == ' ':
                grid[y][x] = '#'
        for _ in range(int(self.size * self.size * 0.05)):  # 5% monsters
            y, x = random_position(self.size)
            if grid[y][x] == ' ':
                grid[y][x] = Monster(random.randint(10, 50))
        for _ in range(int(self.size * self.size * 0.05)):  # 5% treasure chests
            y, x = random_position(self.size)
            if grid[y][x] == ' ':
                grid[y][x] = TreasureChest()
    def display(self, player_position):
        for y in range(self.size):
            for x in range(self.size):
                if (y, x) == player_position:
                    print('P', end=' ')
                elif (y, x) == self.door_position:
                    print('D', end=' ')
                else:
                    print(self.grid[y][x], end=' ')
            print()
    def is_walkable(self, position):
        y, x = position
        return self.grid[y][x] == ' ' or (y, x) == self.door_position
    def interact(self, player):
        y, x = player.position
        if isinstance(self.grid[y][x], Monster):
            monster = self.grid[y][x]
            player.adjust_hp(-monster.hp)
            self.grid[y][x] = ' '  # Remove monster after interaction
        elif isinstance(self.grid[y][x], TreasureChest):
            chest = self.grid[y][x]
            player.adjust_hp(chest.restore_hp())
            self.grid[y][x] = ' '  # Remove chest after interaction
        elif (y, x) == self.door_position:
            print("You have reached the door! Level Complete!")
    def is_level_complete(self, player_position):
        return player_position == self.door_position