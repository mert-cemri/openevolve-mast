'''
Defines the Level class to manage objects, difficulty, and conditions for level completion.
'''
import random
from gameobject import GameObject
class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.objects = []
        self.time_limit = max(30 - level_number * 2, 10)
        self.gold_requirement = 50 + (level_number - 1) * 20
    def generate_objects(self):
        self.objects.clear()
        num_gold = random.randint(3, 5)
        num_rocks = random.randint(2, 4) + self.level_number // 2
        num_diamonds = random.randint(0, 2)
        positions_taken = set()
        for _ in range(num_gold):
            position = self.get_unique_position(positions_taken)
            self.objects.append(GameObject("Gold", random.randint(10, 30), position, random.uniform(1, 2)))
        for _ in range(num_rocks):
            position = self.get_unique_position(positions_taken)
            self.objects.append(GameObject("Rock", random.randint(1, 5), position, random.uniform(2, 4)))
        for _ in range(num_diamonds):
            position = self.get_unique_position(positions_taken)
            self.objects.append(GameObject("Diamond", random.randint(40, 60), position, random.uniform(0.5, 1)))
        print("Objects generated for this level:")
        for obj in self.objects:
            print(f"{obj.type} at position {obj.position}, value: {obj.value}, weight: {obj.weight:.2f}")
    def get_unique_position(self, positions_taken):
        position = random.randint(1, 9)
        while position in positions_taken:
            position = random.randint(1, 9)
        positions_taken.add(position)
        return position
    def check_completion(self, level_gold):
        return level_gold >= self.gold_requirement