'''
Object class to represent objects that can be collected.
'''
class Object:
    def __init__(self, value, reel_time, position):
        self.value = value
        self.reel_time = reel_time
        self.position = position