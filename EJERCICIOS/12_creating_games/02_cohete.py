print("02 - COHETE\n")
"""
Haz un juego que comience con un cohete en el centro de la pantalla. Permite al
usuario mover el cohete hacia arriba, abajo, derecha o izquierda sin salirse de
la misma.
"""

import sys
import pygame

class MyGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Rocket")

        self.rocket = Rocket(self)


    def run_game(self):
        while True:
            # check keyboard events
            self._check_events()

            # update rocket's position
            self.rocket.update()

            self._update_screen()
            pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        # exit the game
        if event.key == pygame.K_q:
            sys.exit()
        # start moving
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True


    def _check_keyup_events(self, event):
        # stop moving
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False


    def _update_screen(self):
        self.screen.fill((128, 128, 128))
        self.rocket.blitme()


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


if __name__ == '__main__':
    mg = MyGame()
    mg.run_game()