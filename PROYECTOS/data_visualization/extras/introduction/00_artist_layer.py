from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

fig = Figure()
canvas = FigureCanvas(fig)

# Create 10.000 random numbers using numpy
import numpy as np
x = np.random.randn(10_000)

# Create an axes artist
ax = fig.add_subplot(111)
# NOTE - 111: creates 1 row, 1 column and uses the 1st cell in the grid for the
# location of the new axes

# Generate the histogram
ax.hist(x, 100)
# NOTE - 100 = create 100 bins

# Add a title to the figure and save it
ax.set_title("Normal distribution with $\mu=0, \sigma=1$")
fig.savefig("./03_extras/00_introduction/plots/histogram.png")