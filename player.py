import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        # Just change the rotation directly
        self.rotation += dt  # PLAYER_TURN_SPEED is used in update()

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer = max(0, self.timer - dt)

        if keys[pygame.K_a]:
            self.rotate(-PLAYER_TURN_SPEED * dt)  # Add PLAYER_TURN_SPEED
        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED * dt)   # Add PLAYER_TURN_SPEED
        if keys[pygame.K_w]:
            self.move(dt)   # Fly forward
        if keys[pygame.K_s]:
            self.move(-dt)   # Go backwards
        if keys[pygame.K_SPACE]:
            self.shoot()   # Shooting

    def move(self, dt):
        # Use (0, -1) to match the triangle method
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Create a forward direction vector based on player's rotation
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        velocity = forward * 500  # Use constant speed (500)

        if self.timer > 0:
            return

        # Create the shot
        shot = Shot(self.position.x, self.position.y, velocity)

        # Append the shot to the game's shot group (example: `self.shots`)
        self.shots.add(shot)

        self.timer = PLAYER_SHOOT_COOLDOWN