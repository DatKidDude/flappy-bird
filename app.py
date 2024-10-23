import pygame 
import sys


def main():
    # Constant Variables
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 800
    FPS = 60

    # Initialize pygame modules
    pygame.init()

    # Create the screen and set screen title
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    # Create pygame clock instance
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        
        pygame.display.update()

        clock.tick(FPS)

if __name__ == "__main__":
    main()