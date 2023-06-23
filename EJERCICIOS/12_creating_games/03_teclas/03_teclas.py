print("03 - TECLAS\n")
"""
Crea un archivo Pygame que cree una pantalla vacía. Haga un bucle de eventos en
el que imprima el atributo 'event.key' siempre que se detecte un evento del
tipo pygame.KEYDOWN.

Ejecute el programa y vea qué responde Pygame.
"""

import sys
import pygame


class MyGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 700))
        self.screen_rect = self.screen.get_rect()

        self.screen.fill((128, 128, 128), self.screen_rect)
        
        pygame.display.set_caption("Teclas")

    
    def run_game(self):
        while True:
            self._check_events()

            pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)


if __name__ == '__main__':
    mg = MyGame()
    mg.run_game()