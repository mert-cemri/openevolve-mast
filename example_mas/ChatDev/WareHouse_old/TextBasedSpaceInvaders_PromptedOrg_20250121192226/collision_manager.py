'''
CollisionManager class to handle collision detection between bullets and aliens.
'''
class CollisionManager:
    def __init__(self, bullets, aliens):
        self.bullets = bullets
        self.aliens = aliens
    def check_collisions(self):
        for bullet in self.bullets[:]:
            for alien in self.aliens[:]:
                if bullet.rect.colliderect(alien.rect):
                    self.bullets.remove(bullet)
                    self.aliens.remove(alien)
                    break