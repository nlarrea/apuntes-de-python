import pygame

class Ship():
    def __init__(self, main_game):
        super().__init__()
        
        self.screen = main_game.screen
        self.screen_rect = main_game.screen.get_rect()

        self.image = pygame.image.load('./img/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)
        self.ship_speed = 1.2

        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ship_speed
        
        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)