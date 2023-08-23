# Visualizar Datos - Trabajar con APIs

<div id='index'></div>

* [Usar una API web](#usar-una-api-web)
* [Git y GitHub](#git-y-github)
    * [Solicitar datos realizando una llamada a la API](#solicitar-datos-realizando-una-llamada-a-la-API)
    * [Instalar Requests](#instalar-requests)


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

