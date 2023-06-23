import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, main_game):
        super().__init__()

        self.screen = main_game.screen

        self.image = pygame.image.load('./img/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True