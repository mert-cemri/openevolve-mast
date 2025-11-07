'''
Level class for managing level logic.
'''
import time
class Level:
    def __init__(self, minimum_gold, time_limit):
        self.minimum_gold = minimum_gold
        self.time_limit = time_limit
        self.current_gold = 0
        self.start_time = time.time()
    def check_completion(self, claw, objects):
        current_time = time.time()
        if current_time - self.start_time >= self.time_limit:
            return True
        for obj in objects:
            if claw.grabbing and claw.is_claw_on_object(obj):
                self.current_gold += obj.value
                objects.remove(obj)
                claw.reel_in()
        return self.current_gold >= self.minimum_gold