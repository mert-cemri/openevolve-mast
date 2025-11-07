'''
CollisionManager class for handling collision detection.
'''
class CollisionManager:
    def check_collision(self, bird, pipes):
        if bird.rect.top <= 0 or bird.rect.bottom >= 600:
            return True
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                return True
        return False