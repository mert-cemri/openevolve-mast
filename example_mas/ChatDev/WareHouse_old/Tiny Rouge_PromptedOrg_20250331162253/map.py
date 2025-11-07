'''
Map class to generate and manage the game map, including walls, floor tiles, and ensuring a valid path exists.
'''
import random
from monster import Monster
from treasure import Treasure
class Map:
    def __init__(self):
        self.grid = self.generate_map()
        self.start_position = (0, 0)
        self.exit_position = (79, 79)
        self.monsters = self.place_monsters()
        self.treasures = self.place_treasures()
    def generate_map(self):
        # Initialize the grid with walls
        grid = [['#' for _ in range(80)] for _ in range(80)]
        # Create a path using DFS or BFS
        path = self.create_path((0, 0), (79, 79))
        # Mark the path on the grid
        for x, y in path:
            grid[y][x] = '.'
        return grid
    def create_path(self, start, end):
        # Implement a pathfinding algorithm to create a path from start to end
        path = []
        stack = [start]
        visited = set()
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            path.append(current)
            if current == end:
                break
            x, y = current
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            random.shuffle(neighbors)
            for neighbor in neighbors:
                nx, ny = neighbor
                if 0 <= nx < 80 and 0 <= ny < 80 and neighbor not in visited:
                    stack.append(neighbor)
        return path
    def is_floor_tile(self, position):
        x, y = position
        return self.grid[y][x] == '.'
    def is_exit_reached(self, position):
        return position == self.exit_position
    def place_monsters(self):
        monsters = []
        while len(monsters) < 10:
            x, y = random.randint(1, 78), random.randint(1, 78)
            if self.is_floor_tile((x, y)):
                monsters.append(Monster((x, y)))
        return monsters
    def place_treasures(self):
        treasures = []
        while len(treasures) < 5:
            x, y = random.randint(1, 78), random.randint(1, 78)
            if self.is_floor_tile((x, y)):
                treasures.append(Treasure((x, y)))
        return treasures
    def check_encounters(self, player):
        # Check for monster encounters
        for monster in self.monsters[:]:
            if player.position == monster.position:
                player.hp -= monster.hp
                print(f"Encountered a monster! Player HP: {player.hp}")
                self.monsters.remove(monster)  # Remove the monster after encounter
        # Check for treasure encounters
        for treasure in self.treasures[:]:
            if player.position == treasure.position:
                player.hp += treasure.heal_amount
                print(f"Found a treasure! Player HP: {player.hp}")
                self.treasures.remove(treasure)  # Remove the treasure after encounter