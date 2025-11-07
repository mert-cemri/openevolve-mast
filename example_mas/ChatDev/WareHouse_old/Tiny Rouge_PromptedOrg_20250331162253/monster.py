'''
Monster class to represent monsters, including attributes like position and health.
'''
class Monster:
    def __init__(self, position):
        self.position = position
        self.hp = 10  # Simplified monster HP