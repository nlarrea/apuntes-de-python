# Visualizar Datos - Descargar Datos

<p id="index">He aquí un pequeño índice de los pasos a seguir:</p>

* [El formato CSV](#el-formato-csv)
    * [Analizar los encabezados de archivos CSV](#analizar-encabezados-de-archivos-csv)
    * [Analizar los encabezados y sus posiciones](#analizar-los-encabezados-y-sus-posiciones)
    * [Extraer y leer datos](#extraer-y-leer-datos)
    * [Trazar datos en un gráfico de temperatura](#trazar-datos-en-un-gráfico-de-temperatura)
    * [El módulo datetime](#el-módulo-datetime)
        * [Dibujar fechas](#dibujar-fechas)
        * [Dibujar espacios de tiempo más largos](#dibujar-espacios-de-tiempo-más-largos)
    * [Trazar una segunda serie de datos](#trazar-una-segunda-serie-de-datos)
    * [Sombrear un área en el gráfico](#sombrear-un-área-en-el-gráfico)
    * [Comprobar errores](#comprobar-errores)

* [Mapear conjuntos de datos globales - JSON](#mapear-conjuntos-de-datos-globales---json)
    * [Descargar datos de los terremotos](#descargar-datos-de-los-terremotos)
    
    * [Examinar datos JSON](#examinar-datos-json)
    
    * [Crear una lista de todos los terremotos](#crear-una-lista-de-todos-los-terremotos)
    
    * [Extraer las magnitudes](#extraer-las-magnitudes)
    
    * [Extraer ubicaciones](#extraer-ubicaciones)
    
    * [Crear un mapa mundial](#crear-un-mapa-mundial)
        * [Una forma diferente de especificar datos](#una-forma-diferente-de-especificar-datos)
        * [Customizar el tamaño de los marcadores](#customizar-el-tamaño-de-los-marcadores)
        * [Otras escalas de color](#otras-escalas-de-color)
        * [Añadir un texto de hover](#añadir-un-texto-de-hover)

<br/>

<hr/>

<hr/><br/>


<div align='right'><a href='#index'>Volver arriba</a></div>

En este apartado, vamos a ver cómo descargar datos de la web y crear visualizaciones con ellos.

Se puede encontrar una cantidad enorme de datos en la web. Estos datos pueden encontrarse en diversos formatos, pero los que vamos a trabajar en esta sección son los archivos CSV (*comma separated values*) y JSON. Vamos a usar Matplotlib para crear visualizaciones con estos datos.

<br/>

<hr/><br/>


# El formato CSV

Una forma muy sencilla de almacenar información es guardarla en un archivo separando los datos con comas. He aquí un ejemplo:

```csv
"USW00025333", "SITKA AIRPORT", "AK US", "2014-01-01", "0.45",, "48", "38"
```

<br/>

> Esa línea indica que el 1 de enero de 2014, en el aeropuerto de Sitka, Alaska, se registró una precipitación de 0.45 pulgadas, la temperatura máxima fue de 48 grados y la temperatura mínima fue de 38 grados.

<br/>

Vamos a comenzar con los datos proporcionados sobre el aeropuerto de Sitka, Alaska. Estos datos se pueden descargar en [la página de GitHub del libro](https://github.com/ehmatthes/pcc/blob/master/chapter_16/sitka_weather_07-2014.csv).

Crearemos un directorio llamado `download_data_section` y dentro de este otra carpeta llamada `data`. El archivo CSV que contiene los datos ([`sitka_weather_07-2018_simple.csv`](https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv)) lo guardaremos dentro de esta carpeta `data`.

<br/>

<hr/><br/>


## Analizar los encabezados de archivos CSV

En python se puede utilizar un módulo estandar (`csv`) para trabajar con este tipo de archivos. Vamos a comenzar analizando la primera línea del archivo, que contiene una serie de encabezados que describen los datos que contiene el archivo, para ello, crearemos el archivo `sitka_highs.py` y añadiremos el siguiente código:

```python
# sitka_highs.py

import csv

filename = "download_data_section/data/sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
```

<br/>

En primer lugar, importamos el módulo `csv` e indicamos el directorio y el nombre del archivo que queremos analizar.

Después, creamos un *reader* del archivo. El módulo CSV contiene un método `next()` que devuelve la siguiente línea del archivo cuando se le pasa un objeto *reader*. En este caso, la primera línea del archivo contiene los encabezados, por lo que la guardamos en la variable `header_row`.

El objeto `reader` procesa la primera línea de valores separados por comas, y guarda cada uno como un elemento en una lista.

Si ejecutamos el archivo desde la terminal, obtendremos la siguiente salida:

```
['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
```

<br/>

<hr/><br/>


## Analizar los encabezados y sus posiciones

Para ver mejor los datos del archivo, imprimiremos cada encabezado y su posición:

```python
# sitka_highs.py

# ...

with open(filename) as f:
    # ...
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
```

<br/>

Si ejecutamos el archivo, obtendremos la siguiente salida:

```
0 STATION
1 NAME
2 DATE
3 PRCP
4 TAVG
5 TMAX
6 TMIN
```

<br/>

<hr/><br/>

## Extraer y leer datos

Ahora que sabemos qué columnas de datos necesitamos, vamos a leer esos datos.

Para empezar, leeremos la temperatura alta de cada uno de los dóas:

```python
# sitka_highs.py

# ...

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get high temperatures from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)
```

<br/>

Hemos creado una lista vacía y realizado un bucle que recorre cada una de las filas del archivo. El objeto `reader` continúa desde donde se queda en el archivo CSV y devuelve automáticamente cada línea después de su posición actual. Como ya hemos leído los encabezados, el bucle comenzará desde la segunda línea, que es donde comienzan los datos como tal.

En cada vuelta del bucle obtenemos los datos correspondientes al índice `5`, es decir, al encabezado `TMAX`, y guardaremos los datos en `highs`.

Este es el resultado obtenido que se almacena en la lista `highs`:

```
[62, 58, 70, 70, 67, 59, 58, 62, 66, 59, 56, 63, 65, 58, 56, 59, 64, 60, 60, 61, 65, 65, 63, 59, 64, 65, 68, 66, 64, 67, 65]
```

<br/>

Con esto, hemos obtenido la temperatura máxima de cada fecha y hemos guardado los valores en una lista. Con esto, ahora podemos crear una visualización de los datos.

<br/>

<hr/><br/>

## Trazar datos en un gráfico de temperatura

Para visualizar los datos de temperatura que tenemos, primero crearemos un gráfico simple utilizando `Matplotlib`:

```python
# sitka_highs.py

# ...
import matplotlib.pyplot as plt

# Read file and save data in 'highs' list
# ...

# Plot the high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot
plt.title("Daily high temperatures, July 2018", fonsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
```

<br/>

Vamos a dibujar las temperaturas altas en rojo y las bajas en azul, así que a la hora de crear el gráfico, indicamos que queremos que sea `c='red'`. Después, creamos un título y unas etiquetas para los datos del gráfico, aunque no hemos colocado las etiquetas a los ejes como tal porque más adelante indicaremos las fechas.

Si ejecutamos el código, veremos cómo se muestra un gráfico simple de color rojo indicando las temperaturas obtenidas del archivo.

<br/>

<hr/><br/>

## El módulo datetime

Como hemos mencionado antes, vamos a añadir fechas a nuestro gráfico para que sea más útil. La primera fecha del archivo está en la segunda fila del mismo.

Las fechas van a ser leídas como **strings**, así que necesitamos convertirlas a objetos de tipo fecha. Podemos crear un objeto que represente la fecha `July 1, 2018` a partir del string `"2018-07-01"` haciendo uso del método `strptime()` del módulo `datetime`:

```
>>> from datetime import datetime
>>> first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
>>> print(first_date)
2018-07-01 00:00:00
```

<br/>

Esos son los pasos a seguir:

1.  Importar la clase `datetime` del módulo `datetime`.
2.  Llamar al método `strptime()` utilizando un string que contenga la fecha deseada. (*El segundo argumento le dice a Python cuál es el formato del string.*)

<br/>

Para conocer los tipos de datos o formatos disponibles, se puede consultar esta tabla:

| Argumento | Significado (Ejemplo)                    |
| :-------: | :--------------------------------------- |
|   `%A`    | Nombre de la semana (*Monday*)           |
|   `%B`    | Nombre del mes (*January*)               |
|   `%m`    | Mes, como número (*del 01 al 12*)        |
|   `%d`    | Día del mes, como número (*del 01 al 31*) |
|   `%Y`    | Año, utilizando 4 dígitos (*2023*)       |
|   `%y`    | Año, utilizando 2 dígitos (*23*)         |
|   `%H`    | Hora, en formato 24 horas (*00 a 23*)    |
|   `%I`    | Hora, en formato 12 horas (*00 a 12*)    |
|   `%p`    | `AM` ó `PM`                              |
|   `%M`    | Minutos (*00 a 59*)                      |
|   `%S`    | Segundos (*00 a 59*)                     |

<br/><br/>

### Dibujar fechas

Ahora que sabemos esto, podemos importar el módulo a nuestro proyecto, extraer las fechas de nuestros datos y dibujarlas:

```python
# sitka_highs.py

# ...
from datetime import datetime

# ...

with open(filename) as f:
    # ...
    
    # Get dates and high temperatures from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        
        dates.append(current_date)
        highs.append(high)

# Plot the high temperatures
# ...
ax.plot(dates, highs, c='red')

# Format plot
# plt.xlabel...
fig.autofmt_xdate()
# ...
```

<br/><br/>

### Dibujar espacios de tiempo más largos

Vamos a añadir más información para completar nuestro gráfico. Para ello, vamos a descargar el archivo [`sitka_weather_2018_simple.csv`](https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv), el cual contiene los datos meteorológicos de todo un año.

Ahora podemos generar un gráfico para el tiempo de todo el año:

```python
# sitka_highs.py

# ...

filename = "download_data_section/data/sitka_weather_2018_simple.csv"

# ...
plt.title("Daily high temperatures - 2018", fontsize=24)
# ...
```

<br/>

Con estos dos pequeños cambios, estaríamos mostrando los datos relacionados a las temperaturas de todo un año en lugar de las de un mes.

<br/>

<hr/><br/>

## Trazar una segunda serie de datos

Podemos hacer nuestro gráfico mucho más informativo si le añadimos las temperaturas bajas. Para ello, necesitamos extraer las temperaturas bajas del archivo correspondiente y añadirlas a nuestro gráfico. Esto lo haremos en un archivo nuevo llamado `sitka_highs_lows.py` que partirá con el mismo código que el visto en el apartado anterior, aquí se ve el código al completo:

```python
# sitka_highs_lows.py

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# filename = "download_data_section/data/sitka_weather_07-2018_simple.csv"
filename = "download_data_section/data/sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

<br/>

<hr/><br/>

## Sombrear un área en el gráfico

Habiendo añadido dos series de datos al gráfico, ahora podemos examinar los rangos de temperaturas de cada día. Vamos a añadir un toque final al gráfico añadiéndole un sombreado entre los datos superiores e inferiores.

Para conseguirlo, vamos a utilizar el método `fill_between()`, el cual toma una serie de los valores `x` y dos series de valores `y` y rellena el espacio entre ambos:

```python
# sitka_highs_lows.py

# ...

# Plot the high temperatures
# ...
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# ...
```

<br/>

>   `alpha` sirve para controlar la transparencia.
>
>   * Un valor `alpha` de `0` significa **completamente transparente**.
>   * Un valor `alpha` de `1` (*default*) significa **completamente opaco**.

<br/>

Este código hace que se vea con mayor claridad la diferencia entre temperaturas mínimas y máximas a lo largo de los días del año.

<br/>

<hr/><br/>

## Comprobar errores

A estas alturas, podemos ejecutar el código del archivo `sitka_highs_lows.py` sin ningún tipo de problema. Sin embargo, en algunos lugares, la forma de recoger la información y, por tanto, de almacenarla, no es la misma.

En esta ocasión vamos a trabajar con un nuevo archivo de datos llamado [`death_valley_2018_simple.csv`](https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/the_csv_file_format/data/death_valley_2018_simple.csv). En primer lugar, vamos a añadir las siguientes líneas a un nuevo archivo llamado `death_valley_highs_lows.py` para ver qué encabezados tiene este nuevo archivo desde el cual vamos a importar los datos:

```python
# death_valley_highs_lows.py

import csv

filename = "./data/dead_valley_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
```

<br/>

He aquí el *output* de este nuevo código:

```
0 STATION
1 NAME
2 DATE
3 PRCP
4 TMAX
5 TMIN
6 TOBS
```

<br/>

El valor de las fechas (`date`) se sigue encontrando en el índice 2, sin embargo, las temperaturas mínima y máxima se han pasado a los índices 4 y 5 respectivamente. Por ello, deberemos modificar los índices de estos valores en nuestro código.

Se ha eliminado del archivo uno de los datos de la temperatura para ver qué ocurre si falta uno de estos datos. Vamos a añadir las siguientes líneas al código:

```python
# death_valley_highs_lows.py

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "download_data_section/data/death_valley_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)   

plt.show()
```

<br/>

Si ejecutamos el código, obtenemos lo siguiente:

```
Traceback (most recent call last):
  File "C:\Users\larre\Documents\NAIA\OpenBootcamp\4-Python\open-python\PROYECTOS\data_visualization\download_data_section\death_valley_highs_lows.py", line 15, in <module>
    high = int(row[4])
ValueError: invalid literal for int() with base 10: ''
```

<br/>

Como se puede observar, el hecho de que falten datos de temperaturas en el archivo provoca errores del tipo `ValueError` por intentar convertir una cadena vacía en un número con la función `int()`.

Una posible solución a este error es realizar lo siguiente:

```python
# death_valley_highs_lows.py

# ...
with open(filename) as f:
    # ...
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# ...
```

<br/>

Con este código, cada vez que examinamos una línea, tratamos de obtener las temperaturas mínimas y máximas. En aquellos casos en los que falte algún dato, Python alzará un `ValueError`, el cual manejaremos a través de mostrar un mensaje por pantalla mostrando la información del dato que falta.

Al ejecutar el código, obtenemos el siguiente mensaje por consola:

```
Missing data for 2018-02-18 00:00:00
```

<br/>

A parte de esto, vemos que se muestra el gráfico con los datos de las temperaturas mínimas y máximas. *¿Por qué?* Porque hemos hecho que cada vez que se produzca un error, el programa sea capáz de seguir funcionando simplemente mostrando un mensaje indicando cuál es el dato que falta.

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

# Mapear conjuntos de datos globales - JSON

En esta sección vamos a ver cómo descargar datos que representen todos los terremostos que han ocurrido en el mundo a lo largo de un mes concreto. Con esto, conseguiremos un mapa que muestre la localización exacta del terremoto y cuán grave ha sido.

Esta información estará contenida en el formato `.json`, por lo que haremos uso de la librería `json`. Además, utilizando la herramienta de creación de mapas de Plotly, podremos crear imágenes que muestren perfectamente la distribución de dichos terremotos.

<br/>

<hr/><br/>

## Descargar datos de los terremotos

Vamos a descargar el archivo [`eq_1_day_m1.json`](https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/mapping_global_data_sets/data/eq_data_1_day_m1.json) al archivo en el que estamos almacenando todos nuestras descargas de datos (la carpeta `data`).

Sabemos que los terremotos están categorizados según su magnitud en la escala Richter. Este archivo incluye datos de los terremotos de magnitud M1 o superiores.

<br/>

<hr/><br/>

## Examinar datos JSON

Al abrir el archivo descargado, veremos que el contenido del mismo es muy denso y difícil de leer.

Este formato es más apropiado para máquinas que para personas, sin embargo, podemos ver que contiene varios diccionarios.

Gracias al módulo `json` podremos trabajar y formatear los datos del archivo `.json` para que los datos que contiene sean mucho mas legibles. Vamos a comenzar añadiendo las siguientes líneas al archivo `eq_explore_data.py`:

```python
# eq_expolore_data.py

import json

# Explore the structure of the data
filename = "download_data_section/data/eq_data_1_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = "download_data_section/data/generated/readable_eq_data.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent=4)
```

<br/>

En primer lugar, importamos el módulo `json` para cargar los datos correctamente y, después, los almacenamos en la variable `all_eq_data`. La función `json.load()` convierte los datos del archivo en un formato que Python entiende: **un diccionario**.

Después, creamos un nuevo archivo en el que guardamos el mismo contenido pero en un formato mucho más legible. La función `json.dump()` toma un objeto JSON y un archivo, y almacena el contenido del objeto JSON en dicho archivo.

Si ejecutamos el código y abrimos el nuevo archivo generado (`readable_eq_data.json`), veremos que ahora es mucho más fácil leer la información.

**La primera parte del nuevo archivo** muestra una sección bajo el nombre de `metadata`, que nos indica cuándo se han generado esos datos, nos muestra un título y la cantidad de terremotos que han sido registrados en las últimas 24h (158 terremotos). La información de los mismos se encuentra bajo una lista `features`. La estructura está formada de tal forma que cada ítem de la lista corresponde a un terremoto.

He aquí la información obtenida del primer terremoto del archivo:

```
{
    "type": "Feature",
    "properties": {
        "mag": 0.96,
        "place": "8km NE of Aguanga, CA",
        "time": 1550360775470,
        "updated": 1550360993593,
        "tz": -480,
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ci37532978",
        "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci37532978.geojson",
        "felt": null,
        "cdi": null,
        "mmi": null,
        "alert": null,
        "status": "automatic",
        "tsunami": 0,
        "sig": 14,
        "net": "ci",
        "code": "37532978",
        "ids": ",ci37532978,",
        "sources": ",ci,",
        "types": ",geoserve,nearby-cities,origin,phase-data,",
        "nst": 32,
        "dmin": 0.02648,
        "rms": 0.15,
        "gap": 37,
        "magType": "ml",
        "type": "earthquake",
        "title": "M 1.0 - 8km NE of Aguanga, CA"
    },
    "geometry": {
        "type": "Point",
        "coordinates": [
            -116.7941667,
            33.4863333,
            3.22
        ]
    },
    "id": "ci37532978"
},
```

<br/>

*   **`properties`:** muestra mucha información sobre el terremoto. Estamos interesados sobre todo en la magnitud del mismo, lo cual se muestra en la propiedad `mag`. También nos interesa el `title`, que ofrece una pequeña descripción de la ubicación del mismo.
*   **`geometry`:** esta sección nos ayuda a conocer dónde ha tendo lugar el terremoto. Necesitaremos esta información para mapear el evento.

<br/>

<hr/><br/>

## Crear una lista de todos los terremotos

Antes de nada, vamos a crear una lista que contenga toda la información acerca de los terremotos. Para ello, modificaremos el archivo `eq_explore_data.py` de la siguiente manera:

```python
# eq_explore_data.py

# ...

with open(filename) as f:
    # ...

all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))
```

<br/>

Con esas dos líneas, obtenemos los datos asociados a la clave `features` del archivo, el cual recordemos que se trata de una lista con los terremotos. Si imprimimos la longitud de esta lista nueva, veremos que la salida muestra el valor `158`, que es la misma cantidad que hemos visto anteriormente en el `metadata` del archivo.

<br/>

<hr/><br/>

## Extraer las magnitudes

Ya tenemos la lista que contiene toda la información acerca de los terremotos, por lo que podemos extraer la magnitud de cada uno de ellos. Para ello, añadiremos las siguientes líneas al archivo `eq_explore_data.py`:

```python
# eq_explore_data.py

# ...

mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    mags.append(mag)

print(mags[:10])
```

<br/>

Con este código extraemos todas las magnitudes y las almacenamos en la variable `mags`. A continuación, imprimimos las 10 primeras magnitudes para ver cómo se muestran:

```
[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
```

<br/>

<hr/><br/>

## Extraer ubicaciones

Para extraer las ubicaciones, vamos a aprovechar el bucle anterior y vamos a modificarlo de la siguiente manera:

```python
# eq_explore_data.py

# ...

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
```

<br/>

Tras ejecutar el nuevo código, obtenemos la siguiente salida:

```
[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
[-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
[33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]
```

<br/>

<hr/><br/>

## Crear un mapa mundial

Con la información que hemos extraído, podemos crear un simple mapa mundial con los datos. Para ello, vamos a crear un nuevo archivo llamado `eq_world_data.py` donde vamos a copiar el código del archivo anterior y a modificarlo de la siguiente manera:

```python
# eq_world_data.py

# ...
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# ...
for eq_dict in all_eq_dicts:
    # ...

# Map the earthquakes
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="download_data_section/data/generated/global_earthquakes.html")
```

<br/>

Hemos importado los módulos necesarios para crear el mapa y hemos creado una lista que contiene un objeto `Scattergeo` que contiene las coordenadas de los terremotos.

Después, creamos un objeto `Layout` que contiene el título del mapa y, por último, creamos un diccionario que contiene los datos y el diseño del mapa. Este diccionario se pasa a la función `offline.plot()` para que cree el mapa.

Con todo esto, hemos creado un mapa muy simple que puede ser mejorado aplicando nuevos estilos que veremos en apartados posteriores.

<br/><br/>

### Una forma diferente de especificar datos

Antes de configurar el gráfico, vamos a ver una forma ligeramente diferente de especificar los datos para un gráfico de Plotly. En el código, tenemos los datos definidos en una única línea, de esta forma:

```python
data = [Scattergeo(lon=lons, lat=lats)]
```

<br/>

Ésta, probablemente, sea la forma más simple de definir los datos para nuestro gráfico, sin embargo, no es el mejor de los métodos. He aquí otra forma equivalente de hacerlo:

```python
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats
}]
```

<br/>

De esta manera, toda la información sobre los datos se estructura como pares *clave-valor* en un **diccionario de Python**.

<br/><br/>

### Customizar el tamaño de los marcadores

Cuando tratamos de imaginar cómo queremos que sea el mapa, una cosa que queda clara es que queremos que los usuarios sean capaces de obtener la información de él de forma rápida y clara. Para ello, hay que asegurarse de que sean capaces de ver y leer correctamente los datos.

Por ello, vamos a modificar el tamaño de los marcadores de la siguiente manera:

```python
# ...

# Map the earthquakes
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [5 * mag for mag in mags]
    }
}]
# ...
```

<br/>

Como se puede observar, Plotly ofrece una gran variedad de opciones para customizar los mapas y gráficos que se generen.

Queremos que los `marker` tengan como tamaño 5 veces la magnitud del terremoto, por lo que haremos uso de la propiedad *list comprehension* propia de las listas de Python para que se encargue de realizar la multiplicación por cada magnitud y almacene los datos en una nueva lista.

Si ejecutamos el código ahora, veremos que se muestran unos círculos de mayor tamaño para cada uno de los terremotos.

<br/><br/>

### Customizar los colores de los marcadores

Además del tamaño, también podemos customizar los colores de los mismos. Como ejemplo, ahora tomaremos otro archivo que muestre los terremotos de los últimos 30 días en lugar de 24 horas. El nuevo archivo se llama [`eq_data_30_day_m1.json`](https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/mapping_global_data_sets/data/eq_data_30_day_m1.json), el cual descargaremos de ese enlace y depositaremos en nuestra carpeta de archivos.

A continuación, realizaremos lo siguiente:

```python
# eq_world_map.py

# ...
filename = "download_data_section/data/eq_data_30_day_m1.json"

# ...

# Map the earthquakes
data = [{
    # ...
    "marker": {
        # ...
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"}
    }
}]
# ...
```

<br/>

En primer lugar, modificamos la dirección del archivo con el que trabajar. Después, la propiedad `color` dice a Plotly qué magnitud es la que hay que colorear, que en este caso, es `mags`.

Hecho esto, indicamos qué escala de colores debe ser usada con `colorscale`, seleccionando la opción `Viridis`, que muestra una escala que va desde el azul oscuro a un amarillo claro. Además, usamos `reversescale: True` porque queremos que indique con color claro las magnitudes más bajas y de oscuro las más grandes.

> Para ver qué otras escalas disponibles hay, puedes consultarlas en [el siguiente apartado](#otras-escalas-de-color).

No solo se ha añadido color al mapa, sino que se ha puesto también a modo *leyenda* una barra de color que indica a qué hacen referencia los colores, por lo que tiene como título `"Magnitude"`.

<br/><br/>

### Otras escalas de color

Si queremos saber qué escalas de colores hay disponibles, podemos crear y ejecutar el siguiente programa:

```python
# show_color_scales.py

from plotly import colors

for key in colors.PLOTLY_SCALES.keys():
    print(key)
```

<br/>

Plotly almacena las escalas de color en el módulo `colors`, por lo que lo importamos e imprimimos cada una de las opciones:

```
Greys
YlGnBu
Greens
YlOrRd
Bluered
RdBu
Reds
Blues
Picnic
Rainbow
Portland
Jet
Hot
Blackbody
Earth
Electric
Viridis
Cividis
```

<br/>

¡Siéntete libre de probar cualquiera de las opciones para personalizar el mapa a tu gusto!

<br/><br/>

### Añadir un texto de hover

Para terminar con este mapa y, por tanto, esta sección, veremos cómo añadir cierto texto informativo para que éste aparezca al hacer *hover* sobre el mapa (*cuando pasamos el ratón por encima*).

La longitud y la latitud son datos que se muestran ya por defecto, sin embargo, queremos que se muestren la magnitud y una breve descripción de la localización más próxima también.

Para esto, haremos lo siguiente:

```python
# eq_world_map.py

# ...

maps, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    # ...
    title = eq_dict["properties"]["title"]
    
    # ...
    hover_texts.append(title)
    
# Map the earthquakes
data = [{
    # ...,
    "text": hover_texts,
    # ...
}]
# ...
```

<br/>

La idea es mostrar la magnitud y una breve información sobre el lugar, sin embargo, la propiedad `title` ya nos ofrece ambas, por lo que podemos añadírselo sin problemas.

Ejecutando el código ahora, se puede comprobar que todo funciona correctamente.