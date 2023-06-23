# Data Visualization

<div id="index"></div>

* [Instalar Matplotlib](#instalar-matplotlib)
* [Trazar un sencillo gráfico de líneas](#trazar-un-sencillo-gráfico-de-líneas)
    * [Modificar la etiqueta y la línea](#modificar-la-etiqueta-y-la-línea)


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

