'''
Game class to manage the game state and loop.
'''
import time
from claw import Claw
from object import Object
from display import Display
class Game:
    def __init__(self):
        self.claw = Claw()
        self.objects = [Object("gold", 100, 5), Object("rock", 10, 10)]
        self.display = Display(self.claw, self.objects)
        self.min_gold_value = 100
        self.time_limit = 60  # seconds
        self.start_time = time.time()
    def start_game(self):
        while True:
            self.claw.move()
            self.display.update_display()
            action = input("Press 'g' to grab or 'c' to continue: ")
            if action.lower() == 'g':
                grabbed_object = self.claw.grab(self.objects)
                if grabbed_object:
                    print(f"You grabbed a {grabbed_object.type} worth {grabbed_object.value}!")
                else:
                    print("Nothing was grabbed.")
            if self.check_win_condition():
                break
            time.sleep(1)  # Simulate time passing
    def check_win_condition(self):
        current_time = time.time()
        if current_time - self.start_time > self.time_limit:
            print("Time's up!")
            return True
        total_gold_value = sum(obj.get_value() for obj in self.objects if obj.is_collected and obj.type == "gold")
        if total_gold_value >= self.min_gold_value:
            print("You win!")
            return True
        return False