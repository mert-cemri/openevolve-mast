'''
Game class to manage the overall game state and loop.
'''
from claw import Claw
from object import Object
from display import Display
import time
class Game:
    def __init__(self):
        self.claw = Claw()
        self.objects = [Object(10, 2, 3), Object(20, 3, 7), Object(5, 1, 5)]  # Example objects with positions
        self.display = Display(self.claw, self.objects)
        self.min_gold_value = 30
        self.current_gold_value = 0
        self.time_limit = 60  # seconds
        self.start_time = time.time()
    def start_game(self):
        while not self.check_win_condition():
            if not self.claw.current_object:  # Only move if not reeling an object
                self.claw.move()
                self.display.update_display()  # Update display after moving
                input("Press Enter to grab...")  # Wait for user input to grab
                if self.claw.grab(self.objects):
                    time.sleep(self.claw.current_object.reel_time)  # Simulate reeling time
                    self.current_gold_value += self.claw.current_object.value
                    self.claw.current_object = None  # Reset after grabbing
            time.sleep(1)  # Simulate time passing
    def check_win_condition(self):
        if self.current_gold_value >= self.min_gold_value:
            print("You win!")
            return True
        if time.time() - self.start_time > self.time_limit:
            print("Time's up!")
            return True
        return False