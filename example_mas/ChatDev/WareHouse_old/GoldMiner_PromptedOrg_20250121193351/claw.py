'''
Claw class to represent the claw's movement and grabbing functionality.
'''
import time
class Claw:
    def __init__(self):
        self.position = (0, 0)
        self.grabbed_object = None
    def move_left(self):
        # Implement logic to move the claw left
        if self.position == (10, 10):
            self.position = (5, 5)
        elif self.position == (5, 5):
            self.position = (0, 0)
    def move_right(self):
        # Implement logic to move the claw right
        if self.position == (0, 0):
            self.position = (5, 5)
        elif self.position == (5, 5):
            self.position = (10, 10)
    def grab(self, obj):
        if self.grabbed_object is None:
            self.grabbed_object = obj
            obj.grabbed = True
            self.reel_in(obj)
    def reel_in(self, obj):
        # Simulate reeling in time based on object's weight
        time_to_reel = obj.get_weight()
        print(f"Reeling in {obj} taking {time_to_reel} seconds.")
        time.sleep(time_to_reel)  # Add delay to simulate reeling time