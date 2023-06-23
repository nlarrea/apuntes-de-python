import pygame

class Rocket:
    def __init__(self, my_game):
        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()

        # load the rocket and get its rect
        self.image = pygame.image.load('./img/rocket.png')
        self.rect = self.image.get_rect()
        # set the rocket position at the middle center of the screen
        self.rect.center = self.screen_rect.center

        # initial values
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.rocket_speed = 1.5

        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        # update the ricket's x & y values, not rects
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.rocket_speed

        # update rect object
        self.rect.x = self.x
        self.rect.y = self.y

    
    def blitme(self):
        # draw rocket at its current location
        self.screen.blit(self.image, self.rect)