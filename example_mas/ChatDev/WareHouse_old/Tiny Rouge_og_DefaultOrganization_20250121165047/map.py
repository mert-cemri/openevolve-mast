'''
Defines the Map class and related functionalities.
'''
import pygame
from random import choice, randint
from monster import Monster
from chest import Chest
from door import Door
class Map:
    def __init__(self):
        self.tiles = [['floor' for _ in range(80)] for _ in range(80)]
        self.start_position = (0, 0)
        self.place_objects()
    def place_objects(self):
        # Use a maze generation algorithm to ensure a path exists
        self.generate_maze()
        # Place monsters and chests randomly on the floor
        for _ in range(20):
            x, y = choice(range(80)), choice(range(80))
            if self.tiles[x][y] == 'floor':
                if choice([True, False]):
                    self.tiles[x][y] = Monster((x, y), randint(5, 15))
                else:
                    self.tiles[x][y] = Chest((x, y))
    def generate_maze(self):
        # Initialize all tiles as walls
        self.tiles = [['wall' for _ in range(80)] for _ in range(80)]
        # Start DFS from the start position
        stack = [(0, 0)]
        self.tiles[0][0] = 'floor'
        while stack:
            x, y = stack[-1]
            neighbors = self.get_unvisited_neighbors(x, y)
            if neighbors:
                nx, ny = choice(neighbors)
                self.tiles[nx][ny] = 'floor'
                self.tiles[(nx + x) // 2][(ny + y) // 2] = 'floor'  # Remove wall between
                stack.append((nx, ny))
            else:
                stack.pop()
        # Ensure the door is reachable
        self.tiles[79][79] = Door((79, 79))
    def get_unvisited_neighbors(self, x, y):
        neighbors = []
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 80 and 0 <= ny < 80 and self.tiles[nx][ny] == 'wall':
                neighbors.append((nx, ny))
        return neighbors
    def is_walkable(self, position):
        x, y = position
        return isinstance(self.tiles[x][y], (str, Chest, Door))
    def get_tile(self, position):
        x, y = position
        return self.tiles[x][y]
    def next_level(self):
        # Logic to move to the next level
        self.__init__()  # Reinitialize the map for the next level
    def draw(self, screen):
        for x in range(80):
            for y in range(80):
                color = (255, 255, 255) if self.tiles[x][y] == 'floor' else (0, 0, 0)
                if self.tiles[x][y] == 'wall':
                    color = (128, 128, 128)
                elif isinstance(self.tiles[x][y], Monster):
                    color = (255, 0, 0)
                elif isinstance(self.tiles[x][y], Chest):
                    color = (255, 215, 0)
                elif isinstance(self.tiles[x][y], Door):
                    color = (0, 0, 255)
                pygame.draw.rect(screen, color, (x * 10, y * 10, 10, 10))