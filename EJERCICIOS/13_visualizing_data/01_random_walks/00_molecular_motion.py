print("02 - MOVIMIENTO MOLECULAR\n\n")
"""
Modifica el código del archivo 'rw_visual.py' sustituyendo 'ax.scatter()' por
'plt.plot()'. Pasa los valores 'rw.x_values' y 'rw.y_values' e incluye el
'linewidth'. Usa 5_000 puntos en lugar de 50_000.
"""

# RandomWalk class:

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
            # decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


# exercise:

import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    ax.plot(
        rw.x_values,
        rw.y_values,
        linewidth=3
    )

    # set chart title
    ax.set_title("Molecular movement", fontsize=24)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == "n":
        break