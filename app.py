import pygame 
from pygame.sprite import Group
from bird import Bird
import sys


def load_image(file, scale=None):
    """
    Loads in image files

    If scale argument is passed, change the size of the image

    Parameters:
    -----------
    file: str
        The file path to the image in the current directory
    
    scale: tuple(int, int), optional
        (width: int, height: int)

    Returns:
    --------
        A pygame surface object
    """
    try:
        surface = pygame.image.load(file)
        if scale:
            surface = pygame.transform.scale(surface, scale)
    except pygame.error:
        raise SystemExit(f"Could not load image '{file}': {pygame.get_error()}")
    return surface.convert()


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

    bird = Bird(screen)

    allsprites = Group((bird))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        allsprites.update()

        allsprites.draw(screen)
        
        pygame.display.update()

        clock.tick(FPS)

if __name__ == "__main__":
    main()