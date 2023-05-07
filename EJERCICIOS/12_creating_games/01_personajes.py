print("01 - PERSONAJES\n")
"""
Busca una imagen bitmap de algún personaje de un videojuego que te guste. Crea
una clase que dibuje ese personaje en el centro de la pantalla. Asegúrate de
que el fondo de la imagen concuerde con el fondo de pantalla, o al revés.
"""

import sys
import pygame

# main game
class MyGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Game Character")

        self.bg_color = (130, 140, 130)

        self.marcus = Character(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.marcus.blitme()

            pygame.display.flip()


# character
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


if __name__ == '__main__':
    gc = MyGame()
    gc.run_game()