'''
Display class to handle rendering the game state to the screen.
'''
class Display:
    def __init__(self, claw, objects):
        self.claw = claw
        self.objects = objects
    def render(self):
        print(f"Claw position: {self.claw.position}")
        for obj in self.objects:
            status = "grabbed" if obj.grabbed else "available"
            print(f"Object at {obj.position} is {status}.")