print("03 - REFACTORIZACIÓN\n\n")
"""
El método 'fill_walk()' es largo. Crea un nuevo método llamado 'get_step()'
para determinar la dirección y distancia de cada paso, después, calcúlalo.
Deberías terminar con dos llamadas a 'get_step()' en 'fill_walk()'.

Esta refactorización sirve para hacer más fácil de leer el método.
"""

from random import choice

class RandomWalk:
    """ A class to generate random walks. """

    def __init__(self, num_points=5000):
        """ Initialize attributes of a walk. """
        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """ Calculate all the points in the walk. """

        # keep taking steps untill the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


    def get_step(self):
        """ Calculate the steps. """
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        
        return direction * distance