import pygame
from constants import *

def main():

    while True:  # Infinite loop!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 


        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main()



