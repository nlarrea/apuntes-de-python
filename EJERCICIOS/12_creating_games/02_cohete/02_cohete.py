print("02 - COHETE\n")
"""
Haz un juego que comience con un cohete en el centro de la pantalla. Permite al
usuario mover el cohete hacia arriba, abajo, derecha o izquierda sin salirse de
la misma.
"""

import sys
import pygame

from rocket import Rocket

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


if __name__ == '__main__':
    mg = MyGame()
    mg.run_game()