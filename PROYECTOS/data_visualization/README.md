# Data Visualization

<div id="index"></div>

* [Instalar Matplotlib](#instalar-matplotlib)
* [Trazar un sencillo gráfico de líneas](#trazar-un-sencillo-gráfico-de-líneas)
    * [Modificar la etiqueta y la línea](#modificar-la-etiqueta-y-la-línea)
    * [Corregir el gráfico](#corregir-el-gráfico)
* [Usar estilos integrados](#usar-estilos-integrados)
* [Trazar y estilizar puntos con scatter()](#trazar-y-estilizar-puntos-con-scatter)
    * [Puntos individuales](#puntos-individuales)
    * [Series de puntos](#series-de-puntos)
* [Calcular datos de automáticamente](#calcular-datos-de-automáticamente)
* [Definir colores customizados](#definir-colores-customizados)
    * [Usar Colormap](#usar-colormap)
* [Guardar gráficos automáticamente](#guardar-gráficos-automáticamente)
* [Caminos aleatorios](#caminos-aleatorios)
    * [Crear la clase RandomWalk](#crear-la-clase-randomwalk)
    * [Elegir direcciones](#elegir-direcciones)
    * [Dibujar el camino aleatorio](#dibujar-el-camino-aleatorio)
    * [Generar varios caminos aleatorios](#generar-varios-caminos-aleatorios)
    * [Estilar el camino](#estilar-el-camino)
        * [Colorear los puntos](#colorear-los-puntos)
        * [Dibujar los puntos de inicio y final](#dibujar-los-puntos-de-inicio-y-final)
        * [Eliminar los ejes](#eliminar-los-ejes)
    * [Incrementar la cantidad de puntos](#incrementar-la-cantidad-de-puntos)
    * [Alterar el tamaño para llenar la pantalla](#alterar-el-tamaño-para-llenar-la-pantalla)
* [Lanzar dados con Plotly](#lanzar-dados-con-plotly)
    * [Instalar Plotly](#instalar-plotly)
    * [Crear la clase Die](#crear-la-clase-die)
    * [Lanzar un dado](#lanzar-un-dado)
        * [Analizar los resultados](#analizar-los-resultados)
        * [Crear un histograma](#crear-un-histograma)
    * [Lanzar dos dados](#lanzar-dos-dados)
    * [Lanzar dados de diferentes caras](#lanzar-dados-de-diferentes-caras)


<br/><hr/>
<hr/><br/>


La visualización de datos implica explorar datos a través de representaciones visuales. Está estrechamente ligada al análisis de datos, que utiluza código para explorar los patrones y conexiones en un conjunto de datos.

Por suerte, Python tiene muchas librerías de visualización de datos, desde librerías de gráficos simples como `matplotlib` (*paquete que instalaremos, a continuación*) hasta librerías de visualización de datos más complejas.

También usaremos un paquete llamado `Plotly`, que crea visualizaciones que funcionan bien en dispositivos digitales, ya que las visualizaciones se redimensionan automáticamente para adaptarse a la pantalla del usuario.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Instalar Matplotlib

Para usar este paquete, debemos instalarlo usando `pip`. Al igual que en el resto de proyectos de este repositorio, usaremos un entorno virtual para instalarlo (`pipenv`).

Para instalar `matplotlib` en nuestro entorno virtual, ejecutamos el siguiente comando en la terminal:

```bash
# desde el directorio donde crearemos el proyecto
pipenv install matplotlib
```

<br/>

> Si no se estuviera usando el entorno virtual:
>
> ```bash
> python -m pip install --user matplotlib
> ```


<br/>

Para ver los tipos de visualizaciones que se pueden realizar con `Matplotlib`, podemos visitar la [galería de ejemplos](https://matplotlib.org/stable/gallery/index.html) de la documentación oficial. Y al hacer clic en cualquiera de los ejemplos, podemos ver el código que se usó para crear la visualización.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Trazar un sencillo gráfico de líneas

Vamos a trazar un gráfico sencillo y lo iremos modificando para ver cómo pueden personalizarse las visualizaciones.

Por ahora, crearemos el archivo `mpl_squares.py` y usaremos una secuencia de números cuadrados como datos a representar:

```python
# mpl_squares.py

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
```

<br/>

En primer lugar, importamos `matplotlib.pyplot` con el alias `plt`. Este módulo contiene una serie de funciones que generan gráficos y trazan diferentes tipos de datos.

A continuación, creamos una lista de números cuadrados y la almacenamos en `squares`. Entonces, llamamos a `plt.subplots()` para que Matplotlib pueda generar uno o más gráficos en la misma figura.

La variable `fig` representa la figura completa o la colección de gráficos que se generan. La variable `ax` representa un solo gráfico en la figura y es la variable que usaremos más a menudo.

Llamamos a `ax.plot(squares)` para trazar los valores de `squares` y usamos `plt.show()` para mostrar el gráfico en una ventana de Matplotlib.


<br/><hr/><br/>


## Modificar la etiqueta y la línea

El gráfico mostrado tras ejecutar el código anterior muestra que el valor de los datos va en aumento. Sin embargo, no se puede decir qué valores específicos corresponden a qué cuadrados.

Vamos a modificar las etiquetas y la línea para que el gráfico sea más fácil de ver:

```python
# mpl_squares.py

# ...
ax.plot(squares, linewidth=3)       # (1)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)     # (2)
ax.set_xlabel("Value", fontsize=14)             # (3)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis="both", labelsize=14)       # (4)

# plt.show()
```

<br/>

* **(1):** se modifica el ancho (*grosor*) de la línea a 3 píxeles.
* **(2):** se añade un título al gráfico.
* **(3):** se añaden etiquetas a los ejes X e Y.
* **(4):** se aumenta el tamaño de las etiquetas de los ejes X e Y.


<br/><hr/><br/>


## Corregir el gráfico

El gráfico que se muestra tras ejecutar el código anterior no es correcto, los datos siguen sin mostrarse bien del todo.

> Muestra el valor de 4*4 como si fuera 25.

Cuando das una secuencia de números a Matplotlib, asume que el primer dato corresponde al valor x de 0, pero nuestros primeros datos corresponden al valor x de 1.

Para corregir esto, podemos pasar a `plot()` los valores de entrada y salida de los datos:

```python
# mpl_squares.py

# ...

input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

# ...
ax.plot(input_values, squares, linewidth=3)

# ...
```

<br/>

Ahora, como le hemos pasado los datos de entrada y de salida a la función `plot()`, Matplotlib no tiene que asumir cómo deben etiquetarse los datos, y el gráfico resultante es correcto.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Usar estilos integrados

Matplotlib trae varios estilos predefinidos que podemos usar para personalizar nuestros gráficos.

Podemos ver qué estilos trae Matplotlib ejecutando el siguiente código desde la terminal (*dentro del directorio del proyecto*):

```python
# si aún no se está usando el entorno virtual
pipenv shell

# ejecutar el intérprete de Python
python
>>> import matplotlib.pyplot as plt
>>> plt.style.available
```

> Para salir del intérprete de Python, ejecutamos `exit()`.

<br/>

Como resultado, obtendremos una lista de estilos disponibles. Para implementar alguno de estos estilos, añadiremos las siguientes líneas de código:

```python
# mpl_squares.py

# ...

plt.style.use('seaborn-v0_8-darkgrid')
# fig, ax = plt.subplots()
# ...
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Trazar y estilizar puntos con scatter

## Puntos individuales

En ocasiones, desearemos trazar puntos individuales en un gráfico. Para ello, usaremos el método `scatter()`, al que se le pasan los valores (x, y) del punto que se quiere trazar.

He aquí un pequeño ejemplo:

```python
# scatter_squares.py

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()

ax.scatter(2, 4)

plt.show()
```

<br/>

Si ejecutamos el archivo, veremos cómo se dibuja un único punto en el gráfico, en el punto (2, 4).

Vamos a estilar el gráfico para añadirle un título y etiquetas a los ejes:

```python
# scatter_squares.py

# ...
# fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)         # (1)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(
    axis="both",
    which="major",
    labelsize=14
)

# plt.show()
```

<br/>

* **(1):** se añade el argumento `s` para establecer el tamaño (*size*) de los puntos.

<br/>

Si ejecutamos el archivo, veremos cómo se dibuja un único punto en el gráfico, en el punto (2, 4).


<br/><hr/><br/>


## Series de puntos

Si queremos trazar series de puntos, podemos pasar a `scatter()` listas separadas de los valores `x` e `y` que queremos trazar de esta manera:

```python
# scatter_squares.py

# ...

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# plt.style.use...
# ...
ax.scatter(x_values, y_values, s=100)

# set chart title and label axes
# ...
```

<br/>

La lista `x_values` contiene los valores de los cuales queremos obtener sus cuadrados, y la lista `y_values` contiene los cuadrados de esos valores.

Si ejecutamos el archivo, veremos cómo se dibujan puntos en el gráfico, en los puntos (1, 1), (2, 4), (3, 9), (4, 16) y (5, 25).


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Calcular datos de automáticamente

En lugar de pasar a `scatter()` las listas de valores `x` e `y`, podemos calcular estos valores automáticamente desde los datos que queremos trazar. Para ello, podemos hacer uso de los bucles propios de Python:

```python
# scatter_squares.py

# ...

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# plt.style.use...
# ...
ax.scatter(x_values, y_values, s=10)

# set chart title and label axes
# ...

# set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])    # (1)

# plt.show...
```

<br/>

* **(1):** Utilizamos el método `axis()` para especificar el rango de cada eje. Este método requiere cuatro valores: los valores mínimos y máximos para el eje x (*[0 - 1100]*) y los valores mínimos y máximos para el eje y (*[0 - 1.100.000]*).


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Definir colores customizados

Para definir los colores de los puntos, basta con pasar el parámetro `c` a `scatter()` con el color que queramos usar:

```python
# scatter_squares.py

# ...

ax.scatter(x_values, y_values, c='red', s=10)

# ...
```

<br/>

O incluso, podemos pasarle una lista de valores para definir nuestro propio color en formato RGB:

```python
# scatter_squares.py

# ...

ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# ...
```


<br/><hr/><br/>


## Usar Colormap

Un colormap es una serie de colores en un gradiente que va de un color inicial a un color final. En los gráficos se usa esta herramienta para enfatizar un patrón en los datos.

Matplotlib incluye una serie de colormaps integrados. Para usarlos, haremos lo siguiente:

```python
# scatter_squares.py

# ...
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes
# ...

# ...
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Guardar gráficos automáticamente

Para guardar un gráfico automáticamente, usaremos el método `savefig()` en lugar de `show()`:

```python
# scatter_squares.py

# ...

plt.savefig("plots/squares_plot.png", bbox_inches="tight")
```

<br/>

El primer argumento es el directorio y el nombre del archivo de la imagen que queremos guardar. El segundo argumento recorta los espacios en blanco que rodean el gráfico.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Caminos aleatorios

Un camino aleatorio es una ruta que no tiene una dirección clara, sino que se determina al azar en cada paso. Los científicos sociales y los economistas han usado caminos aleatorios para intentar predecir los resultados de elecciones, acciones y otros fenómenos complejos.

Vamos a crear un programa que genere un camino aleatorio y lo represente en un gráfico.


<br/><hr/><br/>


## Crear la clase RandomWalk

Vamos a crear el archivo `random_walk.py` y todos los archivos necesarios para esta sección dentro del directorio `random_walk`.

Esta clase sólo necesitará dos métodos inicialmente: `__init__()` y `fill_walk()`, el cual se encargará de calcular los puntos del camino aleatorio.

Comenzamos creando el archivo `random_walk.py` y añadiendo el siguiente código:

```python
from random import choice

class RandomWalk:
    """ A class to generate random walks. """

    def __init__(self, num_points=5000):
        """ Initialize attributes of a walk. """
        self.num_points = num_points

        # all walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
```

<br/>

En primer lugar, importamos la función `choice()` del módulo `random`. Esta función elige un elemento aleatorio de una lista. Dicha lista será la que contenga los posibles valores de los puntos del camino aleatorio.

Como cada camino comienza en el punto (0, 0), inicializamos los atributos `x_values` e `y_values` con una lista que contenga el valor 0.


<br/><hr/><br/>


## Elegir direcciones

Vamos a crear el método `fill_walk()` para que calcule los puntos del camino aleatorio:

```python
# random_walk.py

# ...

class RandomWalk:
    # ...

    def fill_walk(self):
        """ Calculate all the points in the walk. """

        # keep taking steps untill the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # (1) decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # (2) reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # (3) calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # (4)
            self.x_values.append(x)
            self.y_values.append(y)
```

<br/>

En primer lugar, creamos un bucle `while` que se ejecutará mientras no se hayan generado todos los puntos del camino aleatorio.

* **(1):** se utiliza la función `choice()` para elegir una dirección y una distancia para cada eje. Finalmente, el paso se calcula multiplicando la dirección por la distancia.
* **(2):** se rechazan los movimientos que no van a ninguna parte (*que no se mueven*).
* **(3):** se calcula la posición del siguiente punto del camino aleatorio basándose en el último punto de la lista.
* **(4):** se añaden los valores de `x` e `y` a las listas `x_values` e `y_values`.


<br/><hr/><br/>


## Dibujar el camino aleatorio

Para dibujar el camino aleatorio, vamos a crear un nuevo archivo en el mismo directorio que el anterior, llamado `rw_visual.py`:

```python
# rw_visual.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk
rw = RandomWalk()
rw.fill_walk()

# plot the points in the walk
plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
```

<br/>

Comenzamos creando una instancia de la clase `RandomWalk`, la cual hemos importado del archivo anterior. A continuación, llamamos al método `fill_walk()` para que calcule todos los puntos del camino aleatorio.

Finalmente, creamos un gráfico con los puntos del camino aleatorio. Veremos que si ejecutamos dos veces el nuevo código, se generan dos caminos aleatorios diferentes.


<br/><hr/><br/>


## Generar varios caminos aleatorios

Como ya hemos dicho, cada camino aleatorio es diferente. En este apartado vamos a generar varios caminos aleatorios en un mismo código agrupando las siguientes líneas en un bucle:

```python
# rw_visual.py

# ...

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
```

<br/>

Este código genera un camino aleatorio, lo muestra haciendo uso de `Matplotlib` y, **cuando se cierra el gráfico generado**, pregunta al usuario si quiere generar otro camino aleatorio.


<br/><hr/><br/>


## Estilar el camino

En esta sección vamos a customizar los caminos aleatorios. Queremos enfatizar los puntos de tal forma que sea fácil identificar el punto de inicio y el punto final del camino. Así mismo, queremos que se aprecien menos las etiquetas, puesto que en este caso no son tan importantes.


<br/><br/>


### Colorear los puntos

Vamos a usar un `colormap` para colorear los puntos, y eliminaremos el contorno de los mismos. Para ello, pasaremos al argumento `c` una lista con los valores de las posiciones de los puntos. Como éstos son dibujados en orden, la lista solo debe contener los números del 0 a la longitud de la lista de puntos menos 1:

```python
# rw_visual.py

# ...

while True:
    # ...
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=15
    )
    # ...
```

<br/>

Si ejecutamos el código, veremos cómo los puntos se han coloreado en un gradiente de azules, y cómo se ha eliminado el contorno de los mismos.


<br/><br/>


### Dibujar los puntos de inicio y final

Vamos a enfatizar los puntos de inicio y final para distinguir correctamente cuáles son dichos puntos. Para ello, añadiremos las siguientes líneas de código:

```python
# rw_visual.py

# ...

while True:
    # ...
    # ax.scatter(...)

    # emphasize the first and last points
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # plt.show...

    # ...
```

<br/>

Si ejecutamos el código, veremos cómo los puntos de inicio y final se han coloreado en verde y rojo, respectivamente.


<br/><br/>


### Eliminar los ejes

Vamos a eliminar los ejes para que el gráfico sea más limpio. Para ello, añadiremos las siguientes líneas de código:

```python
# rw_visual.py

# ...

while True:
    # ...

    # emphasize the first and last points
    # ...

    # remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # ...
```

<br/>

Si ejecutamos el código, veremos cómo los ejes se han eliminado del gráfico.


<br/><hr/><br/>


## Incrementar la cantidad de puntos

Vamos a incrementar la cantidad de puntos para tener más datos con los que trabajar. Para ello, solo debemos realizar las siguientes modificaciones:

```python
# rw_visual.py

# ...

while True:
    rw = RandomWalk(50_000)
    # ...

    ax.scatter(
        # ...
        s=1
    )

    # ...
```

<br/>

Si ejecutamos el código, veremos cómo se ha incrementado la cantidad de puntos y cómo se ha reducido su tamaño para que el gráfico se vea bien.


<br/><hr/><br/>


## Alterar el tamaño para llenar la pantalla

Es mucho más fácil comunicar a través de un gráfico si éste se ajusta correctamente. Para hacer que el gráfico se ajuste a la pantalla, vamos a modificar la salida de Matplotlib de esta manera:

```python
# rw_visual.py

# ...

while True:
    # ...

    fig, ax = plt.subplots(figsize=(15, 9))

    # ...
```

<br/>

El parámetro `figsize` espera una tupla que indique las dimensiones de la figura en pulgadas.

También es posible pasarle el parámetro `dpi` si conocemos la resolución de la pantalla en la que se va a mostrar el gráfico. De esta manera, Matplotlib ajustará el tamaño de la figura en función de la resolución de la pantalla.

```python
# rw_visual.py

# ...

while True:
    # ...

    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    # ...
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


# Lanzar dados con Plotly

En esta sección, vamos a usar la librería `Plotly` para crear visualizaciones interactivas. Esta es una librería muy útil cuando se pretende crear visualizaciones que van a ser mostradas en buscadores web, porque las visualizaciones se van a ajustar automáticamente a la pantalla.

Para trabajar con esta librería, realizaremos lanzamientos de un dado. Cuando se lanza un dado, cada cara tiene la misma probabilidad de aparecer, sin embargo, al lanzar dos dados, las probabilidades de que ciertos números aparezcan son mayores que las de otros. Vamos a tratar de determinar qué números son más probables que otros al lanzar dos dados.


<br/><hr/><br/>


## Instalar Plotly

Para instalar esta librería, seguiremos el mismo procedimiento visto en secciones anteriores con otras dependencias:

```bash
# desde el directorio donde crearemos el proyecto
pipenv install plotly
```


<br/><hr/><br/>


## Crear la clase Die

Vamos a crear el directorio `rolling_dice` y vamos a almacenar todos los archivos de esta sección en él.

Comenzaremos creando el archivo `die.py` y añadiendo el siguiente código:

```python
# die.py

from random import randint

class Die:
    """ A class representing a single dice. """

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    
    def roll(self):
        """ Return a random value between 1 and number of sides. """
        return randint(1, self.num_sides)
```

<br/>

En primer lugar, importamos la función `randint()` del módulo `random`. Esta función devuelve un número entero aleatorio entre los dos valores que se le pasan como argumentos.

Después, creamos el constructor de la clase `Die` y le pasamos el número de caras que tendrá el dado. Por defecto, el dado tendrá 6 caras.

Además, creamos el método `roll()` que devuelve un número aleatorio entre 1 y el número de caras del dado gracias a la función `randint()`.


<br/><hr/><br/>


## Lanzar un dado

Vamos a crear el archivo `die_visual.py` y añadir el siguiente código:

```python
# die_visual.py

from die import Die

# create a D6
die = Die()

# make some solls and store results in a list
results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
```

<br/>

Hemos importado y creado una instancia del dado cuya clase hemos creado anteriormente. A continuación, hemos creado una lista vacía para almacenar los resultados de los lanzamientos del dado.

Vemos que los resultados de los lanzamientos del dado son números aleatorios entre 1 y 6. Esto significa que el dado se está comportando como se espera.


<br/><br/>


### Analizar los resultados

Vamos a analizar los datos contando cuántas veces aparece cada uno de los valores posibles al lanzar el dado. Para ello, vamos a modificar el archivo `die_visual.py` de la siguiente manera:

```python
# die_visual.py

# ...

for roll_num in range(1000):
    # ...

# analyze the results
frequencies = []

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
```

<br/>

Hemos incrementado el número de lanzamientos del dado a 1000. A continuación, hemos creado una lista vacía para almacenar las frecuencias de cada valor posible.

Si ejecutamos el archivo, obtendremos valores diferentes cada vez. En mi caso:

```bash
[173, 169, 174, 161, 165, 158]
```

<br/>

Podemos observar que cada uno de los valores se repite una cantidad diferente de veces (*puesto que son valores aleatorios*), sin embargo, la diferencia entre la cantidad de veces que se repite cada valor es insignificante.


<br/><br/>


### Crear un histograma

Con la lista de frecuencias que hemos hecho, podemos crear un histograma de los resultados. Un histograma es un gráfico de barras que muestra cuántas veces se repite cada resultado.

Vamos a añadir las siguientes líneas de código al archivo `die_visual.py`:

```python
# die_visual.py

from plotly.graph_objs import Bar, Layout
from plotly import offline

# ...

# visualize the results
x_values = list(range(1, die.num_sides+1))          # (1)
data = [Bar(x=x_values, y=frequencies)]             # (2)

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}

my_layout = Layout(                                 # (3)
    title="Results of rolling one D6 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config
)

offline.plot({"data": data, "layout": my_layout}, filename="d6.html")
```

<br/>

Para crear un histograma necesitamos una barra por cada una de las posibles opciones. Por ello:

* **(1):** Guardamos los posibles valores en la variable `x_values` haciendo uso de la función `range()`.
* **(2):** La clase `Bar` representa un set de datos que va a ser formateado como una barra. Cada objeto espera una lista de valores `x` e `y`. Se debe agrupar dentro de una lista porque pueden haber varios sets de datos.
* **(3):** La clase `Layout` representa lo que se muestra en el gráfico. En este caso, se le pasa el título del gráfico y los títulos de los ejes X e Y.

<br/>

Finalmente, para generar el gráfico, usamos la función `offline.plot()`. Esta función necesita un diccionario con los datos y el layout. Además, le indicamos dónde almacenar el gráfico.

Si ejecutamos el código, veremos que se genera un gráfico interactivo.


<br/><hr/><br/>


## Lanzar dos dados

Vamos a crear el archivo `dice_visual.py`, a añadir el mismo código que en el apartado anterior (*el utilizado para lanzar un único dado*), y a modificar el código para que quede de esta forma:

```python
# dice_visual.py

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create two D6 dice
die_1 = Die()
die_2 = Die()

# make some rolls and store results in a list
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of results"}

my_layout = Layout(
    title="Results of rolling two D6 dice 1000 times",
    xaxis=x_axis_config,
    yaxis=y_axis_config
)

offline.plot({"data": data, "layout": my_layout}, filename="./plots/dice/d6_d6.html")
```

<br/>

Este gráfico muestra los resultados aproximados de lanzar dos dados. Si ejecutamos el gráfico, veremos que los resultados generan una especie de campana de Gauss, lo que significa que los valores menos probables son los que se encuentran en los extremos (*sacar 2 o 12*), y los valores más probables son los que se encuentran en el centro (*sacar un 7*).


<br/><hr/><br/>


## Lanzar dados de diferentes caras

Vamos a modificar el archivo `dice_visual.py` para que lance dos dados de diferentes caras:

```python
# dice_visual.py

# ...

# create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

# make some rolls and store results in a list
# ...

for roll_num in range(50_000):
    # ...

# ...

my_layout = Layout(
    title="Results of rolling a D6 and a D10 50.000 times",
    # ...
)

offline.plot({"data": data, "layout": my_layout}, filename="./plots/dice/d6_d10.html")
```

<br/>

Si ejecutamos el código, veremos que el valor mínimo se mantine en 2, sin embargo, el máximo aumenta a 16 (*6 + 10 caras*).

Los valores más probables ahora son 7, 8, 9, 10 y 11, y los menos probables son 2 y 16.

