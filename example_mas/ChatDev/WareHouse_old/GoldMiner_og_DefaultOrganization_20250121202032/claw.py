'''
Claw class for managing claw movements and interactions.
'''
import pygame
class Claw:
    def __init__(self):
        self.position = [400, 50]
        self.original_position = [400, 50]
        self.direction = 1
        self.speed = 5
        self.grabbing = False
        self.target = None
    def move(self):
        if not self.grabbing:
            self.position[0] += self.direction * self.speed
            if self.position[0] <= 0 or self.position[0] >= 800:
                self.direction *= -1
        else:
            self.reel_in()
    def grab(self, objects):
        for obj in objects:
            if self.is_claw_on_object(obj):
                self.grabbing = True
                self.target = obj
                break
    def reel_in(self):
        if self.target:
            # Calculate the speed reduction based on the object's weight
            reel_speed = max(1, 5 - self.target.weight // 10)
            self.position[1] += reel_speed
            if self.position[1] >= self.target.position[1]:
                self.position = self.original_position[:]
                self.grabbing = False
                self.target = None
    def is_claw_on_object(self, obj):
        claw_x, claw_y = self.position
        obj_x, obj_y = obj.position
        return abs(claw_x - obj_x) < 15 and abs(claw_y - obj_y) < 15
    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (400, 0), self.position, 2)
        pygame.draw.circle(screen, (255, 0, 0), self.position, 10)