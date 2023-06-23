print("05 - ESTRELLAS\n")
"""
Haz que aparezca una cuadrícula de estrellas en la pantalla.
"""

import sys
import pygame

from star import Star

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Estrellas")
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.stars = pygame.sprite.Group()
        self._create_starry_sky()


    def run_game(self):
        while True:
            self._check_events()

            self._update_screen()
            pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and
                event.key == pygame.K_q
            ):
                sys.exit()


    def _create_starry_sky(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        available_space_x = self.screen_rect.width - star_width
        number_stars_x = available_space_x // (2 * star_width)
        available_space_y = self.screen_rect.height - star_height
        number_stars_y = available_space_y // (2 * star_height)

        for row_number in range(number_stars_y):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)


    def _create_star(self, star_number, row_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x

        star.y = star_height + 2 * star_height * row_number
        star.rect.y = star.y

        self.stars.add(star)


    def _update_screen(self):
        self.screen.fill((0, 0, 0))

        self.stars.draw(self.screen)


if __name__ == '__main__':
    ss = Main()
    ss.run_game()