'''
Display class to handle rendering the game state.
'''
class Display:
    def __init__(self, claw, objects):
        self.claw = claw
        self.objects = objects
    def update_display(self):
        # Simple text-based display of the game state
        print(f"Claw position: {self.claw.position}")
        for obj in self.objects:
            status = "collected" if obj.is_collected else "available"
            print(f"Object {obj.type} at {obj.position} is {status}")