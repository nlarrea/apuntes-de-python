# Visualizar Datos - Trabajar con APIs

<div id='index'></div>

* [Usar una API web](#usar-una-api-web)
* [Git y GitHub](#git-y-github)
    * [Solicitar datos realizando una llamada a la API](#solicitar-datos-realizando-una-llamada-a-la-API)
    * [Instalar Requests](#instalar-requests)
    * [Procesar la respuesta de una API](#procesar-la-respuesta-de-una-api)
    * [Trabajar con el diccionario de la respuesta](#trabajar-con-el-diccionario-de-la-respuesta)

<!-- CÓMO HACER LOS ÍNDICES --> 

<!-- * Git y Github -->

<!-- 	* ... -->

<!-- * Hacker News API -->

<!-- 	* ... -->

<br/>

<hr/><hr/><br/>

En esta sección, vamos a escribir un programa capaz de generar una visualización basada en datos que recupere de una API (*Application Programming Interface*) web, para solicitar automáticamente una información concreta a un sitio web y usar dichos datos para generar gráficos.

Como las APIs web son lugares que generalmente permanecen actualizados, utilizando APIs nuestra aplicación no se quedará obsoleta, ya que si se modifica el dato de la API, también lo hará la aplicación que hayamos creado.

<br/>

<hr/><hr/><br/>

## Usar una API web

Una API web es una parte de un sitio web designado a interactuar con programas. Dichos programas utilizan URLs muy concretas para solicitar la información. A esta acción se le llama *llamar a una API*.

La información vendrá facilitada en un formato tipo JSON, CSV o parecidos, es decir, formatos simples para permitir un fácil acceso a la información.

<br/>

<hr/><hr/><br/>

## Git y GitHub

Vamos a basar nuestras visualizaciones en información obtenida de [GitHub](https://github.com/), un sitio que, entre otras cosas, permite a los programadores colaborar en proyectos de código. Vamos a usar la API de GitHub para solicitar información acerca de proyectos de Python almacenados en la plataforma y realizar visualizaciones sobre la popularidad de dichos proyectos.

> GitHub recibe su nombre de [Git](https://git-scm.com/), un sistema de control de versiones. Git ayuda muchísimo a gestionar el trabajo sobre un proyecto, especialmente si se trabaja en grupo, puesto que el trabajo realizado por un sujeto, no perjudica ni modifica el trabajo realizado por otro.
>
> Al implementar una nueva *feature* en un proyecto, Git realiza el seguimiento de los cambios realizados en cada archivo del mismo.

<br/>

Cuando a los usuarios de GitHub les gusta un proyecto (*también conocido como **repositorio***), pueden añadirlo a favoritos o darle una *estrella*. En esta sección vamos a crear un programa capaz de descargar datos automáticamente de los proyectos más valorados sobre Python en GitHub, y crearemos una visualización de ello.

<br/>

<hr/><br/>

### Solicitar datos realizando una llamada a la API

GitHub permite solicitar una cantidad enorme de información a través de la API. Para saber cómo se ve una llamada a una API, introduce el siguiente link en tu navegador:

```
https://api.github.com/search/repositories?q=language:python&sort=stars
```

<br/>

Vamos a explicar este enlace por partes:

* `https://api.github.com/`: dirige la solicitud a la parte de GitHub que responde a las llamadas de la API.
* `search/repositories`: le indica a la API que dirija la búsqueda a través de los repositorios de GitHub (*es decir, que estamos buscando repositorios*).
* `?`: indica que vamos a pasar argumentos para realizar la búsqueda.
* `q=`: la `q` significa *query*, y el signo `=` nos permite comenzar a escribir una consulta. Al utilizar `language:python` decimos que sólo queremos información de aquellos repositorios cuyo lenguaje principal sea Python. Con `&sort=stars` ordenamos el resultado de la consulta en función de la cantidad de estrellas que tienen los repositorios.

<br/>

Realizando la llamada a través del navegador, verás que se encuentran varios millones de repositorios (*la cantidad devuelta en `total_count`*). Sabemos que se ha realizado correctamente la llamada si en la sección `incomplete_results` tenemos como resultado un `false` en lugar de un `true`.  Después, tendremos `items`, que son los que contienen la información de cada uno de los repositorios encontrados.

<br/>

<hr/><br/>

### Instalar Requests

El paquete `requests` permite a Python realizar solicitudes a una página web de forma muy sencilla y examinar la respuesta. Vamos a usar `pip` para instalarlo:

```powershell
# desde el directorio del proyecto
pipenv install requests
```

<br/>

<hr/><br/>

### Procesar la respuesta de una API

Ahora que hemos instalado `requests`, vamos a hacer uso de dicha librería y vamos a ver cómo gestionar la respuesta de una API. Para ello, crearemos un archivo llamado `python_repos.py` con el siguiente código:

```python
# python_repos.py

import requests

# Make an API call and store the response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = { "Accept": "application/vnd.github.v3+json" }

r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable
response_dict = r.json()

# Process results
print(responde_dict.keys())
```

<br/>

Estos son los pasos que se han seguido escribiendo las líneas de código mostradas:

1. Se importa la librería `requests` para poder utilizarla en el proyecto.
2. Se guarda la URL de la llamada a la API en una variable para poder utilizarla a lo largo del archivo.
3. Definimos el encabezado para la API, de esta forma indicamos que queremos usar la versión 3 de la API de GitHub.
4. Usamos la librería `requests` para hacer la petición utilizando los parámetros previamente definidos.
5. El objeto respuesta, `r`, tiene un atributo llamado `status_code`, el cual nos indica si una petición ha sido satisfactoria o no. Imprimimos su valor para asegurarnos de que todo haya salido correctamente.
6. La API devuelve la información en el formato JSON, por lo que convertimos dicha información en un diccionario de Python con el método `json()`.
7. Finalmente, imprimimos las claves del diccionario, al cual hemos llamado `response_dict`.

<br/>

Tras ejecutar el programa, veremos que se obtiene lo siguiente:

```powershell
Status code: 200
dict_keys(['total_count', 'incomplete_results', 'items'])
```

<br/>

> Como el *Status code* tiene un valor de `200`, sabemos que todo ha salido correctamente.
>
> El diccionario que contiene la respuesta tiene tres claves:
>
> * `total_counts`
> * `incomplete_results`
> * `tems`

<br/>

<hr/><br/>

### Trabajar con el diccionario de la respuesta

Habiendo almacenado la respuesta de la API en un diccionario, podemos trabajar con los datos almacenados en el mismo. Vamos a generar una salida que resuma el contenido de la información obtenida:

```python
# python_repos.py

# ...

# Make an API call and store the response
# ...

# Store API responde in a variable
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo)dicts}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

for key in sorted(repo_dict.keys()):
    print(key)
```

<br/>

Explicación:

1. Primero imprimimos el valor asociado al `total_count`, que representa el número total de repositorios de Python en GitHub.
2. El valor asociado a `items` es una lista que contiene una cantidad de diccionarios, donde cada uno contiene información acerca de un único repositorio. Lo que hacemos es almacenar la lista completa en `repo_dicts` e imprimimos la longitud de la lista para saber cuántos repositorios hemos recibido.
3. Obtenemos el primer repositorio de la lista y lo almacenamos en `repo_dict`.
4. Imprimimos la cantidad de claves que tiene dicho diccionario.
5. Imprimimos todas las claves del diccionario para saber qué información tenemos del mismo.

<br/>

Como resultado se obtiene lo siguiente:

```
Status code: 200
Total repositories: 9074612
Repositories returned: 30

Keys: 80
allow_forking
archive_url
archived
assignees_url
	...
url
visibility
watchers
watchers_count
web_commit_signoff_required
```

<br/>

Como se puede observar, la API de GitHub devuelve muchísima información de cada uno de los repositorios: hay `80` claves en `repo_dict`. Mirando estas claves, uno se puede hacer una idea de qué tipo de información puede extraer. Por ejemplo:

```python
# python_repos.py

# ...

# Examine the first repository
repo_dict = repo_dicts[0]


print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")						# name of the project
print(f"Owner: {repo_dict['owner']['login']}")			# owner is a dictionary, we get owner's login name
print(f"Stars: {repo_dict['stargazers_count']}")		# how many stars the project has earned
print(f"Repository: {repo_dict['html_url']}")			# url of the project's repository
print(f"Created: {repo_dict['created_at']}")			# when the repository was created
print(f"Updated: {repo_dict['updated_at']}")			# when was the last time the repository was updated
print(f"Description: {repo_dict['description']}")		# repository's description
```

<br/>

Este es el resultado obtenido (*el resultado varía en función de cuándo se haga la petición a la API, este es el resultado obtenido el día que se escribió esta guía*):

```
Status code: 200
Total repositories: 9463565
Repositories returned: 30

Selected information about first repository:
Name: public-apis
Owner: public-apis
Stars: 252728
Repository: https://github.com/public-apis/public-apis
Created: 2016-03-20T23:49:42Z
Updated: 2023-08-23T22:14:25Z
Description: A collective list of free APIs
```

<br/>

<hr/><br/>

