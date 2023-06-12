import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet. """

    def __init__(self, ai_game):
        """ Initialize the alien and set its starting position. """
        super().__init__()
        self.screen = ai_game.screen

        # load the alien image and set its rect attribute
        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position
        self.x = float(self.rect.x)


    def check_edges(self):
        """ Return if alienis at edge of screen. """
        screen_rect = self.screen.get_rect()

        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    
    def update(self):
        """ Move the alien right or left. """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x