'''
Defines the Level class for managing the level layout and objects.
'''
import pygame
from monster import Monster
from treasure_chest import TreasureChest
from door import Door
class Level:
    def __init__(self):
        self.map = self.generate_map()
        self.start_position = (1, 1)  # Example start position
    def generate_map(self):
        # Generate a map with walls, floors, monsters, chests, and doors
        map = [['floor' for _ in range(80)] for _ in range(80)]
        # Example: Set some walls
        for i in range(80):
            map[0][i] = 'wall'
            map[79][i] = 'wall'
            map[i][0] = 'wall'
            map[i][79] = 'wall'
        # Place a door
        map[78][78] = Door((78, 78))
        # Place some monsters
        map[10][10] = Monster((10, 10), 20)
        map[20][20] = Monster((20, 20), 30)
        # Place some treasure chests
        map[15][15] = TreasureChest((15, 15))
        map[25][25] = TreasureChest((25, 25))
        # Ensure a path from start to door
        self.ensure_path(map)
        return map
    def is_walkable(self, x, y):
        # Check if the position is within bounds
        if 0 <= x < 80 and 0 <= y < 80:
            obj = self.map[y][x]
            # Allow movement if the tile is a floor or contains a non-blocking object
            return isinstance(obj, str) and obj == 'floor' or isinstance(obj, (TreasureChest, Door))
        return False
    def get_object_at(self, x, y):
        return self.map[y][x]
    def draw(self, screen):
        # Draw the level layout
        for y in range(80):
            for x in range(80):
                obj = self.map[y][x]
                if obj == 'wall':
                    pygame.draw.rect(screen, (255, 255, 255), (x * 10, y * 10, 10, 10))
                elif isinstance(obj, Monster):
                    pygame.draw.rect(screen, (255, 0, 0), (x * 10, y * 10, 10, 10))
                elif isinstance(obj, TreasureChest):
                    pygame.draw.rect(screen, (255, 215, 0), (x * 10, y * 10, 10, 10))
                elif isinstance(obj, Door):
                    pygame.draw.rect(screen, (0, 255, 0), (x * 10, y * 10, 10, 10))
    def ensure_path(self, map):
        # Implement a pathfinding algorithm to ensure a path from start to door
        # This is a placeholder for the actual pathfinding logic
        pass