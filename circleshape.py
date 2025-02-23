import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other_shape):
        # Get distance between centers using distance_to
        distance = self.position.distance_to(other_shape.position)
        # Get sum of both radii
        total_radius = self.radius + other_shape.radius
        # If distance is less than total radius, they're colliding!
        return distance <= total_radius