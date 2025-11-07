'''
Map class for generating and rendering the game map with guaranteed valid path.
'''
import random
import pygame
from monster import Monster
from treasure import Treasure
from collections import deque
class Map:
    def __init__(self, size=80):
        self.size = size
        self.grid = [['#' for _ in range(size)] for _ in range(size)]
        self.monsters = []
        self.treasures = []
        self.start_x, self.start_y = 1, 1
        self.door_x, self.door_y = size - 2, size - 2
        self.generate_map()
    def generate_map(self):
        while True:
            # Randomly generate the map
            for x in range(1, self.size - 1):
                for y in range(1, self.size - 1):
                    self.grid[y][x] = '.' if random.random() > 0.2 else '#'
            # Ensure start and door positions are open
            self.grid[self.start_y][self.start_x] = '.'
            self.grid[self.door_y][self.door_x] = 'D'
            # Check if a valid path exists
            if self.is_valid_path():
                break
        # Place monsters and treasures randomly
        placed = 0
        while placed < 50:
            mx, my = random.randint(1, self.size - 2), random.randint(1, self.size - 2)
            if self.grid[my][mx] == '.' and (mx, my) != (self.start_x, self.start_y):
                monster = Monster(mx, my)
                self.monsters.append(monster)
                placed += 1
        placed = 0
        while placed < 30:
            tx, ty = random.randint(1, self.size - 2), random.randint(1, self.size - 2)
            if self.grid[ty][tx] == '.' and (tx, ty) != (self.start_x, self.start_y):
                treasure = Treasure(tx, ty)
                self.treasures.append(treasure)
                placed += 1
    def is_valid_path(self):
        visited = [[False for _ in range(self.size)] for _ in range(self.size)]
        queue = deque()
        queue.append((self.start_x, self.start_y))
        visited[self.start_y][self.start_x] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            x, y = queue.popleft()
            if (x, y) == (self.door_x, self.door_y):
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    if not visited[ny][nx] and self.grid[ny][nx] in ('.', 'D'):
                        visited[ny][nx] = True
                        queue.append((nx, ny))
        return False
    def is_walkable(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.grid[y][x] in ('.', 'D')
    def is_door(self, x, y):
        return x == self.door_x and y == self.door_y
    def render(self, screen, tile_size):
        colors = {'#': (100, 100, 100), '.': (0, 0, 0), 'D': (0, 255, 0)}
        for y in range(self.size):
            for x in range(self.size):
                rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, colors.get(self.grid[y][x], (0, 0, 0)), rect)
        for monster in self.monsters:
            monster.render(screen, tile_size)
        for treasure in self.treasures:
            treasure.render(screen, tile_size)