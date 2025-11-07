'''
Claw class to represent the claw's movement and actions.
'''
import pygame
class Claw:
    def __init__(self):
        self.position = (400, 50)
        self.direction = 1  # 1 for right, -1 for left
        self.speed = 5
        self.grabbing = False
        self.grabbed_object = None
    def move(self):
        if not self.grabbing:
            x, y = self.position
            if x >= 750 or x <= 50:
                self.direction *= -1
            self.position = (x + self.speed * self.direction, y)
    def grab(self, objects):
        if not self.grabbing:
            for obj in objects:
                if self._is_within_grab_range(obj):
                    self.grabbing = True
                    self.grabbed_object = obj
                    break
    def _is_within_grab_range(self, obj):
        claw_x, claw_y = self.position
        obj_x, obj_y = obj.position
        # Calculate the Euclidean distance between the claw and the object
        distance = ((claw_x - obj_x) ** 2 + (claw_y - obj_y) ** 2) ** 0.5
        # Define a threshold distance for grabbing
        grab_threshold = 30
        return distance < grab_threshold
    def update_grab(self, level):
        if self.grabbing and self.grabbed_object:
            # Simulate reeling in the object
            obj_x, obj_y = self.grabbed_object.position
            claw_x, claw_y = self.position
            if obj_y > claw_y:
                self.grabbed_object.position = (obj_x, obj_y - 2)
            else:
                # Update the level's current value
                level.update_current_value(self.grabbed_object.value)
                self.grabbing = False
                self.grabbed_object = None
    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), self.position, (self.position[0], self.position[1] + 50), 2)
        if self.grabbing and self.grabbed_object:
            self.grabbed_object.draw(screen)