print("01 - CIELO AZUL")
"""
Crea un juego con un cielo azul.
"""

import sys
import pygame

class BlueSky:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Blue Sky")

        self.bg_color = (0, 0, 150)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()