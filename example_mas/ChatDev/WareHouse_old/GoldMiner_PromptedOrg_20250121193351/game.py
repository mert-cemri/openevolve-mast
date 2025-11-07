'''
Game class to manage the game loop and win/lose conditions.
'''
from claw import Claw
from object import Object
from display import Display
import time
class Game:
    def __init__(self):
        self.claw = Claw()
        self.objects = [Object(10, 5, (5, 5)), Object(20, 10, (10, 10))]
        self.display = Display(self.claw, self.objects)
        self.min_gold_value = 30
        self.time_limit = 60  # seconds
        self.start_time = time.time()
    def start(self):
        while not self.check_win_condition():
            self.update()
            self.display.render()
            time.sleep(1)  # Simulate time passing
    def update(self):
        # Capture user input for movement and grabbing
        user_input = input("Press 'l' to move left, 'r' to move right, 'g' to grab: ")
        if user_input.lower() == 'l':
            self.claw.move_left()
        elif user_input.lower() == 'r':
            self.claw.move_right()
        elif user_input.lower() == 'g':
            for obj in self.objects:
                if self.claw.position == obj.position and not obj.grabbed:
                    self.claw.grab(obj)
                    break
    def check_win_condition(self):
        current_time = time.time()
        if current_time - self.start_time > self.time_limit:
            print("Time's up!")
            return True
        total_value = sum(obj.get_value() for obj in self.objects if obj.grabbed)
        if total_value >= self.min_gold_value:
            print("You win!")
            return True
        return False