import matplotlib.pyplot as plt

from random_walk import RandomWalk

# keep making new walks, as long as the program is active
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break