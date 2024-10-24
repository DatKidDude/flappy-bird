import pygame 
from pygame.sprite import Group
from bird import Bird
import game_functions as gf
import sys, os
import math


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

    # Load background image and change it's height
    bg = pygame.image.load(os.path.join("assets", "sprites", "background-day.png"))
    bg = pygame.transform.scale(bg, (288, SCREEN_HEIGHT))
    bg_width = bg.get_width()
    
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    scroll = 0

    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
        
        allsprites.update()

        # Get the scroll value so it doesn't reset back to 0
        scroll = gf.scroll_background(screen, bg, bg_width, tiles, scroll)
    
        allsprites.draw(screen)
        # Update screen display
        pygame.display.update()

        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()