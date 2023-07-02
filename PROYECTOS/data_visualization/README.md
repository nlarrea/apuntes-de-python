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


