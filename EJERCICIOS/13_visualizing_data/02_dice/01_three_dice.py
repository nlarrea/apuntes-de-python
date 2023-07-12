print("01 - TRES DADOS\n")
"""
Cuando lanzas tres dados de 6 caras, el menor valor posible es el 3, y el mayor
18. Lanza tres dados de seis caras y muestra qué ocurre.
"""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# create 3 D6
die_1 = Die()
die_2 = Die()
die_3 = Die()


# make some rolls and store results
results = []

for roll_num in range(10_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)


# analyze the results
frequencies = []
max_value = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(3, max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)


# visualize the results
x_values = list(range(3, max_value + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}

my_layout = Layout(
    title="Results of rolling three D6 10_000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config
)

offline.plot({"data": data, "layout": my_layout}, filename="../../EJERCICIOS/13_visualizing_data/02_dice/plots/3_d6.html")
