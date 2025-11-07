'''
Defines the Claw class to manage claw movement, grabbing, and reeling in objects.
'''
import time
class Claw:
    def __init__(self):
        self.position = 0
        self.direction = 1  # 1 for right, -1 for left
        self.speed = 1
    def move(self):
        self.position += self.direction * self.speed
        if self.position >= 10 or self.position <= 0:
            self.direction *= -1
        print(f"Claw position: {self.position}")
    def grab(self, objects):
        closest_object = None
        min_distance = float('inf')
        for obj in objects:
            distance = abs(obj.position - self.position)
            if distance <= 1 and distance < min_distance:
                closest_object = obj
                min_distance = distance
        if closest_object:
            print(f"Automatically grabbing {closest_object.type} (value: {closest_object.value}, weight: {closest_object.weight:.2f})")
            return closest_object
        print("No object within grabbing range.")
        return None
    def reel_in(self, obj):
        print(f"Reeling in {obj.type}...")
        time.sleep(obj.weight)  # Simulate reel-in time based on weight
        if obj.type in ["Gold", "Diamond"]:
            return obj.value
        elif obj.type == "Rock":
            print("Oh no! You grabbed a rock. No gold earned.")
            return 0