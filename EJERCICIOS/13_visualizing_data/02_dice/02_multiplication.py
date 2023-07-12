print("02 - MULTIPLICATION\n")
"""
Al lanzar dos dados, se suman los resultados. Crea un programa que en lugar de
sumar los resultados de los dos dados, los multiplique.
"""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create a D6
die_1 = Die()
die_2 = Die()

# make some solls and store results in a list
results = []

for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_value = die_1.num_sides + die_2.num_sides

for value in range(1, max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
x_values = list(range(1, max_value + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}

my_layout = Layout(
    title="Results of rolling one D6 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config
)

offline.plot({"data": data, "layout": my_layout}, filename="../../EJERCICIOS/13_visualizing_data/02_dice/plots/multiply.html")