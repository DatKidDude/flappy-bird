import pygame
from pygame.sprite import Sprite

class Bird(Sprite):
    """Creates a bird on the screen that the player can move up or down"""

    img_width = 54
    img_height = 44

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Initialize flappy bird image and get its rect
        self.image = pygame.image.load("./assets/sprites/bluebird-midflap.png")
        self.image = pygame.transform.scale(self.image, (self.img_width, self.img_height))
        self.rect = self.image.get_rect()

        # Start the player in the center of the screen
        self.rect.center = self.screen_rect.center


        def update(self):
            pass
