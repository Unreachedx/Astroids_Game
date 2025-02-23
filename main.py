import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

updateable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group,)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:  # Infinite loop!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 

        screen.fill((0, 0, 0))  # Fill the screen with black
        updateable_group.update(dt)
        for sprite in drawable_group:
            sprite.draw(screen)
        

        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Get delta time in seconds


if __name__ == "__main__":
    main()
