'''
Map class to generate and manage the game map.
'''
import random
import heapq
from monster import Monster
from treasure_chest import TreasureChest
from door import Door
class Floor:
    pass
class Map:
    def __init__(self):
        self.width = 80
        self.height = 80
        self.grid = [[Floor() for _ in range(self.width)] for _ in range(self.height)]
        self.start_position = (0, 0)
    def generate_map(self):
        self.grid[0][0] = 'Start'
        self.grid[79][79] = Door()
        path = self.create_path(self.start_position, (79, 79))
        path_set = set(path)
        for _ in range(10):
            x, y = random.randint(0, 79), random.randint(0, 79)
            while (x, y) in path_set:
                x, y = random.randint(0, 79), random.randint(0, 79)
            self.grid[x][y] = Monster()
        for _ in range(5):
            x, y = random.randint(0, 79), random.randint(0, 79)
            while (x, y) in path_set:
                x, y = random.randint(0, 79), random.randint(0, 79)
            self.grid[x][y] = TreasureChest()
    def create_path(self, start, end):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, end)}
        while open_set:
            _, current = heapq.heappop(open_set)
            if current == end:
                return self.reconstruct_path(came_from, current)
            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, end)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    def get_neighbors(self, position):
        x, y = position
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.width and 0 <= ny < self.height]
    def reconstruct_path(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
            self.grid[current[0]][current[1]] = Floor()
        return path
    def is_walkable(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and (isinstance(self.grid[x][y], Floor) or self.grid[x][y] == 'Start')
    def get_object_at(self, position):
        x, y = position
        return self.grid[x][y]
    def display(self, player_position):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == player_position:
                    print('P', end='')
                elif isinstance(self.grid[x][y], Monster):
                    print('M', end='')
                elif isinstance(self.grid[x][y], TreasureChest):
                    print('T', end='')
                elif isinstance(self.grid[x][y], Door):
                    print('D', end='')
                else:
                    print('.', end='')
            print()