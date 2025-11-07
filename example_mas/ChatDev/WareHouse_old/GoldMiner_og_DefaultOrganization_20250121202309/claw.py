'''
Claw class that handles the movement and grabbing mechanics.
'''
import pygame
class Claw:
    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.x = 400
        self.y = 100
        self.direction = 1
        self.grabbed_object = None
    def move(self):
        self.x += self.direction * 5
        if self.x <= 0 or self.x >= 800:
            self.direction *= -1
    def grab(self, objects):
        for obj in objects:
            if abs(self.x - obj.x) < 10 and not self.grabbed_object:
                self.grabbed_object = obj
                break
    def reel_in(self):
        if self.grabbed_object:
            # Set a minimum reeling speed
            reeling_speed = max(1, 5 / self.grabbed_object.weight)
            self.grabbed_object.y -= reeling_speed
            if self.grabbed_object.y <= self.y:
                # Update the score when the object is successfully reeled in
                self.level.score += self.grabbed_object.value
                self.grabbed_object = None
    def draw(self):
        pygame.draw.line(self.screen, (255, 255, 255), (self.x, self.y), (self.x, self.y + 50), 2)
        if self.grabbed_object:
            self.grabbed_object.draw()