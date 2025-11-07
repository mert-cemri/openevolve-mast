'''
Defines the Game class to manage the game loop, level progression, and game state.
'''
import time
from claw import Claw
from level import Level
class Game:
    def __init__(self):
        self.level_number = 1
        self.total_gold = 0
        self.level_gold = 0
        self.claw = Claw()
        self.level = Level(self.level_number)
    def run(self):
        print("Welcome to Gold Miner!")
        while True:
            print(f"\nStarting Level {self.level_number}")
            self.level.generate_objects()
            self.level_gold = 0
            level_time = self.level.time_limit
            start_time = time.time()
            while time.time() - start_time < level_time:
                self.update()
                if self.level.check_completion(self.level_gold):
                    print(f"Level {self.level_number} completed!")
                    break
            if not self.level.check_completion(self.level_gold):
                print("Game Over! You did not meet the gold requirement.")
                break
            self.level_number += 1
            self.level = Level(self.level_number)
        print(f"Game Over! Total gold collected: {self.total_gold}")
    def update(self):
        self.claw.move()
        grabbed_object = self.claw.grab(self.level.objects)
        if grabbed_object:
            gold_earned = self.claw.reel_in(grabbed_object)
            self.total_gold += gold_earned
            self.level_gold += gold_earned
            self.level.objects.remove(grabbed_object)
            print(f"Collected {grabbed_object.type} worth {gold_earned} gold. Level gold: {self.level_gold}, Total gold: {self.total_gold}")
        time.sleep(0.5)  # Slight delay for better readability