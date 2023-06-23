import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, main_game):
        super().__init__()

        self.screen = main_game.screen

        self.width = 15
        self.height = 3
        self.color = (60, 60, 60)
        self.speed = 3.0

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midleft = main_game.ship.rect.midright

        self.x = float(self.rect.x)


    def update(self):
        # update the decimal position
        self.x += self.speed

        # update the rect position
        self.rect.x = self.x


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)