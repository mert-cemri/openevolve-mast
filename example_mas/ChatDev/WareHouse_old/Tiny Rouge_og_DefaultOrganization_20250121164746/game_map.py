'''
GameMap class to generate and manage the game map.
'''
import pygame
import random
class GameMap:
    def __init__(self):
        self.width = 80
        self.height = 80
        self.map = self.generate_map()
        self.start_position = (0, 0)  # Example starting position
    def generate_map(self):
        # Initialize the map with walls
        map = [['wall' for _ in range(self.width)] for _ in range(self.height)]
        # Define start and end points
        start = (0, 0)
        end = (self.width - 1, self.height - 1)
        # Use a maze generation algorithm to carve out a path
        self.carve_path(map, start, end)
        # Place monsters and treasure chests
        self.place_objects(map)
        return map
    def carve_path(self, map, start, end):
        # Simple DFS to ensure a path from start to end
        stack = [start]
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            map[y][x] = 'floor'
            if (x, y) == end:
                break
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in visited:
                    stack.append((nx, ny))
    def place_objects(self, map):
        # Randomly place monsters and treasure chests
        for _ in range(100):  # Example number of objects
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if map[y][x] == 'floor':
                map[y][x] = random.choice(['monster', 'treasure'])
    def is_walkable(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[y][x] in ['floor', 'monster', 'treasure']
        return False
    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map[y][x]
        return 'wall'
    def draw(self, screen):
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile == 'floor':
                    color = (255, 255, 255)
                elif tile == 'monster':
                    color = (255, 0, 0)
                elif tile == 'treasure':
                    color = (0, 255, 255)
                else:
                    color = (0, 0, 0)
                pygame.draw.rect(screen, color, pygame.Rect(x * 10, y * 10, 10, 10))