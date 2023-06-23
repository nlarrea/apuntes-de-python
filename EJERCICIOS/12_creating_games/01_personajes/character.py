import pygame


class Character:
    def __init__(self, gc_game):
        self.screen = gc_game.screen
        self.screen_rect = gc_game.screen.get_rect()

        # Load the image and get its rect
        self.image = pygame.image.load('./img/marcus_fenix.bmp')
        self.rect = self.image.get_rect()
        # position
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)