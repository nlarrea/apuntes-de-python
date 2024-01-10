import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10_000)
plt.hist(x, 100)
plt.title(r"Normal distribution with $\mu=0, \sigma=1$")
plt.savefig("./03_extras/00_introduction/plots/matplotlib_histogram.png")
plt.show()