print("04 - TIRADOR LATERAL\n")
"""
Crea un juego que coloque una nave en el lateral izquierdo de la pantalla y
permita al jugador moverla hacia arriba y hacia abajo.

Haga una nave que dispare una bala que se mueva por toda la pantalla hacia la
derecha cuando el jugador pulse la tecla ESPACIO.

* Asegurarse de que se eliminan las balas cuando desaparecen de la ventana.
"""


import sys
import pygame

from ship import Ship
from bullet import Bullet

class Main:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption("Tirador lateral")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    
    def run_game(self):
        while True:
            self._check_events()

            self.ship.update()
            self._update_bullets()

            self._update_screen()
            pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)


    def _check_keydown_event(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    

    def _check_keyup_event(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def _update_bullets(self):
        # update bullet position
        self.bullets.update()

        # get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
            
            # check if bullets are removed once they disappear
            # print("Number of bullets:", len(self.bullets))
            

    def _update_screen(self):
        self.screen.fill((128, 128, 255))
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


if __name__ == '__main__':
    tl = Main()
    tl.run_game()