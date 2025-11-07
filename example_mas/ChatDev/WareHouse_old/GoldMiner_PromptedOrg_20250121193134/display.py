'''
Display class to handle the display of the game state.
'''
class Display:
    def __init__(self, claw, objects):
        self.claw = claw
        self.objects = objects
    def update_display(self):
        print(f"Claw position: {self.claw.position}")
        print("Objects:")
        for obj in self.objects:
            print(f"Object at position {obj.position} with value {obj.value}")