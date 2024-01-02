# APLICACIONES WEB - Django

> Documentación de Django:
>
> https://docs.djangoproject.com/en/5.0/

<br/>

<div id="index" />

* [Primeros pasos con Django](#django)
* [Configurar el proyecto](#configurar-el-proyecto)
    * [Escribir una especificación](#escribir-una-especificación)
    * [Crear el entorno virtual](#crear-el-entorno-virtual)
    * [Instalar Django](#instalar-django)
    * [Crear un proyecto de Django](#crear-un-proyecto-de-django)
    * [Crear la base de datos](#crear-la-base-de-datos)
    * [Ver el proyecto en el navegador](#ver-el-proyecto-en-el-navegador)
* [Crear una aplicación](#crear-una-aplicación)
    * [Definir los modelos](#definir-los-modelos)
    * [Activar los modelos](#activar-los-modelos)
    * [El sitio Admin de Django](#el-sitio-admin-de-django)
        * [Crear un superusuario](#crear-un-superusuario)
        * [Registrar un modelo usando el sitio admin](#registrar-un-modelo-usando-el-sitio-admin)
        * [Añadir un tema](#añadir-un-tema)
    * [Definir el modelo Entry](#definir-el-modelo-entry)
    * [Migrar el modelo Entry](#migrar-el-modelo-entry)
    * [Registrar el modelo Entry en el sitio admin](#registrar-el-modelo-entry-en-el-sitio-admin)
    * [El intérprete de Django](#el-intérprete-de-django)
* [Crear páginas: La página principal](#crear-páginas-la-página-principal)
    * [Mapear una URL](#mapear-una-url)
    * [Escribir una vista](#escribir-una-vista)
    * [Escribir una plantilla](#escribir-una-plantilla)
* [Escribir páginas adicionales](#escribir-páginas-adicionales)
    * [Herencia de plantillas](#herencia-de-plantillas)
        * [La plantilla base](#la-plantilla-base)
        * [La plantilla hija](#la-plantilla-hija)
    * [Página de temas](#página-de-temas)
        * [Patrón de URL para los temas](#patrón-de-url-para-los-temas)
        * [La vista de los temas](#la-vista-de-los-temas)
        * [La plantilla de los temas](#la-plantilla-de-los-temas)
    * [Páginas de temas individuales](#páginas-de-temas-individuales)
        * [Patrón de URL para los temas individuales](#patrón-de-url-para-los-temas-individuales)
        * [La vista de los temas individuales](#la-vista-de-los-temas-individuales)
        * [La plantilla de los temas individuales](#la-plantilla-de-los-temas-individuales)
        * [Links para las páginas de temas individuales](#links-para-las-páginas-de-temas-individuales)
* [Cuentas de usuario](#cuentas-de-usuario)

<br/>

<hr/><hr/><br/>

<div align='right'>
    <a href="#index">Volver arriba</a>
</div>

# Primeros pasos con Django

Django es un framework de Python para el desarrollo web.

En esta sección, se explica cómo crear un proyecto de Django desde cero, en este caso, una app llamada `Learning Log`, una aplicación que permite a los usuarios registrar los temas sobre los que han aprendido y hacer un seguimiento de los detalles de cada tema.

Vamos a crear los ajustes para la aplicación, y luego crearemos un proyecto de Django que contenga la aplicación.

Gracias a este framework, podemos responder a los requerimientos de los usuarios de forma rápida y sencilla. Podremos manejar datos de una base de datos, y también veremos cómo desplegar la aplicación en un servidor web para que otros puedan usarla.


<br/><hr/>
<hr/><br/>

<div align='right'>
    <a href="#index">Volver arriba</a>
</div>

# Configurar el proyecto

La mejor forma de comenzar un proyecto de Django es crear una descripción general, acompañada de una serie de especificaciones. Después, se creará un entorno virtual para el proyecto.


<br/><hr/><br/>


## Escribir una especificación

La especificación de una aplicación web es una descripción general que describe la funcionalidad de la aplicación y su interfaz. La especificación de `Learning Log` es la siguiente:

> Vamos a crear una aplicación que permita a los usuarios registrar los temas sobre los que han aprendido y hacer un seguimiento de los detalles de cada tema. La página principal de la aplicación debe describir la aplicación y animar a los usuarios a registrarse. Una vez que un usuario se haya registrado e iniciado sesión, podrá crear nuevos temas, añadir nuevas entradas y leer y editar las entradas existentes.


<br/><hr/><br/>


## Crear el entorno virtual

Un entorno virtual es un directorio que contiene una versión específica de Python, así como unos cuantos paquetes adicionales. Vamos a crear un entorno virtual para el proyecto `Learning Log` y a instalar Django en él.

Crearemos el entorno virtual de la siguiente forma:

<div id='activate-venv' />

```bash
# Desde el directorio de Django:
py -m venv ll_env
# Para activar el entorno virtual:
ll_env/Scripts/activate
```

> Si queremos desactivar el entorno virtual, ejecutamos el comando `deactivate`:
>
> ```bash
> deactivate
> ```


<br/><hr/><br/>


## Instalar Django

Para instalar Django, con el **entorno virtual activado** ejecutamos el siguiente comando:

```bash
pip install django
```

<br/>

Esperamos a que se instale y listo, podremos usar Django en nuestro proyecto. Se ha de tener en cuenta que para poder utilizar Django, el entorno virtual ha de estar activado.


<br/><hr/><br/>

## Crear un proyecto de Django

Teniendo el entorno virtual activado, vamos a crear un proyecto de Django con los siguientes comandos:

> Si el entorno virtual está desactivado, se ha de [activar](#activate-venv) antes de ejecutar los siguientes comandos.

```bash
# Desde el directorio de Django:
django-admin startproject learning_log .
```

<br/>

Con el comando de arriba, indicamos que queremos crear un proyecto de Django llamado `learning_log` y que el punto final le dice a Django que cree el proyecto con la estructura de directorios en la que nos encontramos.

Lo que ocurre después de ejecutar el comando es que se crea un directorio llamado `learning_log` que contiene los siguientes archivos:

* `__init__.py`: Un archivo vacío que le dice a Python que trate el directorio como un paquete.
* `settings.py`: Un archivo que le dice a Django cómo comportarse.
* `urls.py`: Un archivo que le dice a Django qué páginas debe crear en respuesta a las solicitudes de los usuarios.
* `wsgi.py`: Un archivo que ayuda a Django a servir los archivos que componen el proyecto en un servidor web.
* `asgi.py`: Un archivo que ayuda a Django a servir los archivos que componen el proyecto en un servidor web.


<br/><hr/><br/>


## Crear la base de datos

Django almacena casi toda la información en una base de datos, por lo que necesitamos crear una base de datos para nuestro proyecto.

Inserta los siguientes comandos por consola:

> Recuerda que el entorno virtual ha de estar [activado](#activate-venv).

```bash
python manage.py migrate
```

<br/>

Cada vez que modificamos la base de datos, estamos pidiendo que se haga una *migración*. Ejecutando la orden `migrate`, estamos pidiendo a Django que se asegure de que la base de datos concuerda con el estado actual del proyecto.

Como es la primera vez que ejecutamos esa orden, Django crea una base de datos SQLite para nosotros. Si miramos el directorio del proyecto, veremos que se ha creado un archivo llamado `db.sqlite3`.

SQLite es una base de datos que se ejecuta en un archivo en lugar de en un servidor. Esto hace que sea ideal para el desarrollo y la prueba de aplicaciones web, o aplicaciones muy sencillas.


<br/><hr/><br/>


## Ver el proyecto en el navegador

Para ver el proyecto en el navegador, ejecutamos el siguiente comando:

```bash
python manage.py runserver
```

<br/>

Veremos un mensaje que dice lo siguiente:

```bash
Starting development server at http://127.0.0.1:8000/
```

<br/>

Para ver el proyecto, copiamos la dirección y la pegamos en el navegador (*o hacemos click sobre ella*). Se puede utilizar también la dirección `http://localhost:8000/`, que es lo mismo que la anterior.

Si queremos terminar el servidor, pulsamos `Ctrl + C` en la terminal donde se está ejecutando.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href="#index">Volver arriba</a>
</div>


# Crear una aplicación

Los proyectos de Django están compuestos por grupos de aplicaciones individuales que trabajan juntas para hacer que el proyecto funcione como un todo.

Por ahora, crearemos una única aplicación que se encargue de gestionar todo lo posible. Más adelante, crearemos otras aplicaciones para gestionar otras partes del proyecto.

Por ahora, deberías mantener el servidor del apartado anterior en ejecución. Abre una nueva terminal y navega al directorio donde se encuentra el archivo `manage.py`. [Activa el entorno virtual](#activate-venv) y ejecuta el siguiente comando:

```bash
python manage.py startapp learning_logs
```

<br/>

El comando `startapp appname` le dice a Django que genere la estructura necesaria para crear una aplicación.

Si miramos el directorio del proyecto ahora, veremos que tenemos la carpeta `learning_logs` que contiene los siguientes archivos:

* `__init__.py`: Un archivo vacío que le dice a Python que trate el directorio como un paquete.
* `admin.py`: Un archivo que nos permite construir una interfaz para gestionar la aplicación a través del sitio web de administración de Django.
* `apps.py`: Un archivo que almacena la configuración de la aplicación.
* `models.py`: Un archivo que nos permite definir los datos que queremos gestionar en nuestra aplicación.
* `tests.py`: Un archivo que nos permite escribir pruebas automáticas para la aplicación.
* `views.py`: Un archivo que nos permite escribir las funciones que gestionan las solicitudes que recibe la aplicación y devuelven una respuesta.
* `migrations/`: Un directorio que Django utiliza para gestionar las migraciones de la base de datos.


<br/><hr/><br/>


## Definir los modelos

Pensemos en nuestros datos por un momento. Cada uno de los usuarios necesitará crear una serie de temas. Cada tema estará asociado a un tema, y esas entradas estarán mostradas como texto. También almacenaremos la fecha y hora en que se creó cada entrada, para que podamos mostrar a los usuarios cuándo se creó cada entrada.

Abre el archivo `models.py` y añade el siguiente código:

```python
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
    
        return self.text
```

<br/>

1. Hemos creado la clase `Topic` que hereda de `Model`, una clase que contiene la funcionalidad básica de los modelos de Django.
2. Hemos definido un atributo `text` que es un objeto `CharField` de Django, un tipo de datos que le indica a Django que reserve una cantidad fija de espacio en la base de datos. En este caso, reservamos un espacio de 200 caracteres.
3. Hemos definido un atributo `date_added` que es un objeto `DateTimeField` de Django, un tipo de datos que le indica a Django que reserve un espacio para almacenar una fecha y hora.
4. Hemos definido un método `__str__()` que devuelve una cadena que representa al modelo. Django utiliza esta representación en muchos lugares, como en la vista de administración. Si no definimos un método `__str__()`, Django devolverá una representación de cadena básica que no es muy útil.


<br/><hr/><br/>


## Activar los modelos

Para usar los modelos que hemos creado, debemos decirle a Django que los incluya en el proyecto. Busca y abre el archivo `settings.py` (*dentro de `learning_log`*). Busca la lista `INSTALLED_APPS` y añade la siguiente línea:

```python
INSTALLED_APPS = [
    # My apps
    "learning_logs",

    # Default django apps
    # ...
]
```

<br/>

Agrupar las aplicaciones en un único lugar ayuda a mantener la organización del proyecto. En este caso, hemos añadido la aplicación `learning_logs` a la lista de aplicaciones instaladas, que es nuestra única aplicación por ahora.

Es importante escribir nuestras aplicaciones antes que las predeterminadas de Django si queremos sobrescribir alguna de las funcionalidades de Django.

Ahora, debemos decirle a Django que modifique la base de datos para incluir la información que acabamos de añadir. Para ello, ejecutamos el siguiente comando:

```bash
python manage.py makemigrations learning_logs
```

<br/>

El comando `makemigrations` le dice a Django que busque las modificaciones que se han hecho en los modelos y que las guarde como una migración. Veremos que se ha añadido un archivo llamado `0001_initial.py` al directorio `migrations` de la aplicación `learning_logs`. Esto crea una tabla para el modelo `Topic` en la base de datos.

Ahora, ejecutamos el siguiente comando para aplicar la migración a la base de datos:

```bash
python manage.py migrate
```

<br/>

Veremos que se muestra un mensaje de confirmación de que se ha aplicado la migración.

Cada vez que modifiquemos los modelos, tendremos que repetir estos tres pasos:

1. Modificar los modelos en `models.py`.
2. Ejecutar `python manage.py makemigrations appname`.
3. Ejecutar `python manage.py migrate`.


<br/><hr/><br/>


## El sitio Admin de Django

Django hace que sea fácil trabajar con los modelos creados a través del *sitio admin*. Sólo los administradores tienen acceso a este sitio, no los usuarios comunes.

En esta sección, vamos a configurar el sitio admin y vamos a usarlo para añadir algunos temas a través del modelo `Topic`.


<br/><br/>


### Crear un superusuario

Django nos permite crear un *superuser*, un usuario que tiene todos los privilegios, y estos privilegios son los que permiten a los usuarios hacer diferentes tareas.

La configuración de privilegios con más restricciones sólo permitiría a los usuarios leer de la página. Normalmente, los usuarios registrados tienen acceso a mayor contenido en una aplicación.

Para crear un superusuario, ejecutamos el siguiente comando:

> Recuerda que el entorno virtual ha de estar [activado](#activate-venv).

```bash
python manage.py createsuperuser
Username (leave blank to use 'user'): ll_admin
Email address:
Password:
Password (again):
Superuser created successfully.
```

<!-- contraseña guardada en .env -->

<br/>

Como se puede observar, se nos piden una serie de datos para crear el superusuario. El nombre de usuario y la contraseña son obligatorios, pero el correo electrónico es opcional.


<br/><br/>


### Registrar un modelo usando el sitio admin

Django incluye algunos modelos de forma automática en el sitio admin, como los modelos `User` y `Group`, pero los modelos que creamos nosotros, deben ser añadidos manualmente.

Cuando creamos la aplicación `learning_logs`, Django creó un archivo llamado `admin.py` en el directorio de la aplicación. Abre este archivo y añade el siguiente código:

```python
from django.contrib import admin

# Register your models here.
from .models import Topic

admin.site.register(Topic)
```

<br/>

Este código importa el modelo `Topic` que queremos registrar y luego usa la función `register()` para decirle a Django que administre nuestro modelo a través del sitio admin.

Ahora, ejecutamos el servidor y abrimos el sitio admin en el navegador. Si el servidor no estaba ya en ejecución, ejecutamos el siguiente comando:

```bash
python manage.py runserver
```

<br/>

A continuación, abrimos el navegador y accedemos a la dirección `http://localhost:8000/admin/`. Veremos una página de inicio de sesión. Introducimos las credenciales del superusuario que creamos anteriormente y pulsamos `Log in`.

Veremos una página que dice `Site administration` donde encontramos los apartados:

* `AUTHENTICATION AND AUTHORIZATION`
    * `Groups`
    * `Users`
* `LEARNING_LOGS`
    * `Topics`


<br/><br/>


### Añadir un tema

Ahora que hemos registrado el modelo `Topic`, podemos añadir algunos temas a través del sitio admin.

Para ello, haz clic en `Topics` para ir a la página de temas (*[localhost:8000/admin/learning_logs/topic/](localhost:8000/admin/learning_logs/topic/)*). Desde aquí, haz clic en `Add topic` (*arriba a la derecha*) y aparecerá un formulario para añadir un nuevo tema. Introduce `Chess` en el primer campo de texto y pulsa `Save`. Veremos que se ha añadido un nuevo tema a la lista.

Habrás sido revuelto a la página donde están los temas donde, ahora verás que el tema `Chess` aparece en la lista.

¡Creemos un segundo tema! Haz clic en `Add topic` y añade `Rock Climbing`. Veremos que se ha añadido un segundo tema a la lista.


<br/><hr/><br/>


## Definir el modelo Entry

Hemos añadido los temas `Chess` y `Rock Climbing`, pero debemos definir un modelo para las entradas de cada tema para que los usuarios puedan añadir entradas a cada uno de ellos. Cada entrada debe ir asociada a un tema concreto.

He aquí el código para el modelo `Entry`:

```python
# models.py

from django.db import models


class Topic(models.Model):
    # ...


class Entry(models.Model):
    """ Something specific learned about a topic. """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """ Return a string representation of the model. """

        return f"{self.text[:50]}..."
```

<br/>

1. Hemos creado la clase `Entry` que hereda de `Model`, una clase que contiene la funcionalidad básica de los modelos de Django, al igual que hicimos con el modelo `Topic`.
2. Hemos definido un atributo `topic` que es un objeto `ForeignKey` de Django, un tipo de datos que le indica a Django que relacione cada entrada con un tema específico. Cada tema se asocia con una clave primaria, un ID único que Django utiliza para referirse a cada entrada. *Es decir, hemos relacionado cada entrada `Entry` con un tema `Topic`*.
3. Hemos definido un atributo `text` que es un objeto `TextField` de Django, un tipo de datos que le indica a Django que reserve un espacio para almacenar un texto largo.
4. Hemos definido un atributo `date_added` que es un objeto `DateTimeField` de Django, un tipo de datos que le indica a Django que reserve un espacio para almacenar una fecha y hora.
5. Hemos definido una clase `Meta` que contiene metadatos para administrar un modelo. En este caso, le decimos a Django que use la forma plural de `entry` para referirse a más de una entrada. Sin esta clase, Django usaría `Entrys` como nombre para más de una entrada.
6. Hemos definido un método `__str__()` que devuelve una cadena que representa al modelo. Django utiliza esta representación en muchos lugares, como en la vista de administración.


<br/><hr/><br/>


## Migrar el modelo Entry

Ahora que hemos definido el modelo `Entry`, debemos decirle a Django que modifique la base de datos para incluir la información que acabamos de añadir.

Esto es algo que ya hemos visto anteriormente, por lo que simplemente introducimos los siguientes comandos:

```bash
python manage.py makemigrations learning_logs
python manage.py migrate
```

<br/>

Se habrá generado una nueva migración llamada `0002_entry.py` en el directorio `migrations` de la aplicación `learning_logs`. Esto crea una tabla para el modelo `Entry` en la base de datos.


<br/><hr/><br/>


## Registrar el modelo Entry en el sitio admin

Ahora debemos modificar el archivo `admin.py` para registrar el modelo `Entry`:

```python
# admin.py

from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
```

<br/>

Si accedemos de nuevo a la página de administración (*[localhost:8000/admin/](localhost:8000/admin/)*), veremos que ahora tenemos el apartado `Entries` en la sección `LEARNING_LOGS`.

Tenemos dos opciones para añadir entradas:

1. Seguir los mismos pasos utilizados para los `Topics`:
    1. Hacer clic en `Entries` para ir a la página de entradas (*[localhost:8000/admin/learning_logs/entry/](localhost:8000/admin/learning_logs/entry/)*).
    2. Hacer clic en `Add entry` (*arriba a la derecha*) y aparecerá un formulario para añadir una nueva entrada.
2. Hacer clic en `Add` sin entrar en la página de entradas.

<br/>

En cualquier caso, cuando aparezca el formulario, deberíamos ver un menú desplegable con los temas que hemos creado. Si hacemos clic en el menú desplegable, veremos que aparecen los temas `Chess` y `Rock Climbing`.

Escogemos el tema `Chess` y añadimos el siguiente texto:

```text
The opening is the first part of the game, roughly the first ten
moves or so. In the opening, it’s a good idea to do three things
—bring out your bishops and knights, try to control the center
of the board, and castle your king.
Of course, these are just guidelines. It will be important to
learn when to follow these guidelines and when to disregard
these suggestions.
```

<br/>

Cuando hayamos escrito o pegado el texto en el campo, pulsamos `Save` y veremos que se ha añadido una nueva entrada a la lista. Aquí, veremos el beneficio de usar `text[:50]` como la representación de cadena para cada entrada. En lugar de ver el texto completo de la entrada, vemos los primeros 50 caracteres, seguidos de puntos suspensivos.

Ahora, añadimos una segunda entrada para el tema `Chess`:

```text
In the opening phase of the game, it’s important to bring out
your bishops and knights. These pieces are powerful and
maneuverable enough to play a significant role in the
beginning moves of a game.
```

<br/>

Y añade una entrada más, esta vez para el tema `Rock Climbing`:

```text
One of the most important concepts in climbing is to keep
your weight on your feet as much as possible. There’s a myth
that climbers can hang all day on their arms. In reality, good
climbers have practiced specific ways of keeping their weight
over their feet whenever possible.
```

<br/>

Estas tres entradas nos permitirán tener algo de contenido para trabajar mientras desarrollamos la aplicación.


<br/><hr/><br/>


## El intérprete de Django

Ahora que hemos introducido algunos datos con los que poder trabajar, vamos a explorar esos datos de forma programática. Para ello, vamos a utilizar el intérprete de Django, el cual es un entorno estupendo para testear el proyecto.

He aquí un ejemplo de cómo usar el intérprete de Django para explorar los datos que hemos introducido:

```bash
python manage.py shell
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
>>>
```

> Usa `exit()` para salir del intérprete cuando lo desees.

<br/>

El comando `shell` le dice a Django que abra un intérprete de Python que nos permita trabajar con los datos del proyecto. El intérprete de Django es un entorno de prueba estupendo, ya que nos permite trabajar con los datos de la aplicación sin tener que escribir código para crear una vista.

En el ejemplo mostrado, hemos importado el modelo `Topic` del módulo `learning_logs.models`. A continuación, hemos usado el método `objects.all()` para obtener todos los objetos `Topic` de la base de datos. El resultado es un objeto `QuerySet` que contiene todos los temas de la base de datos.

Podemos iterar sobre un `QuerySet` para ver cada tema individualmente:

```bash
>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
...
1 Chess
2 Rock Climbing
>>>
```

<br/>

Hemos almacenado el `QuerySet` en la variable `topics` y luego hemos iterado sobre la variable para mostrar el ID y el texto de cada tema.

Si conoces el ID de un objeto en particular, puedes utilizar el método `objects.get()` para obtener ese objeto y mostrar su información:

```bash
>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2023, 12, 30, 10, 44, 23, 406934, tzinfo=datetime.timezone.utc)
>>>
```

<br/>

Podemos, también, observar las entradas relacionadas a un tema concreto. Anteriormente, hemos definido el atributo `topic` en el modelo `Entry` como un objeto `ForeignKey`, una conexión entre cada entrada y un tema. Django puede usar esta conexión para obtener las entradas asociadas a un tema en particular:

```bash
>>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>]>
>>>
```

<br/>

Para obtener los datos de una entrada a través de una `ForeignKey`, se utiliza el nombre (*en minúsculas*) del modelo relacionado seguido de `_set`. Esto le dice a Django que obtenga las entradas asociadas al tema que hemos almacenado en `t`.

Utilizaremos esta sintaxis más adelante cuando comencemos a crear las páginas de los usuarios. El intérprete es muy útil para asegurarse de recibir la información deseada. No usaremos mucho el intérprete a lo largo del desarrollo de la aplicación, pero es muy recomendable que la sigas usando para aprender y explorar las oportunidades que ofrece, además de seguir las buenas prácticas.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href="#index">Volver arriba</a>
</div>


# Crear páginas: La página principal

Crear páginas web con Django consta de tres pasos:

1. Definir las URLs de la aplicación.
2. Escribir las *vistas* de la aplicación.
3. Escribir las plantillas de la aplicación.

>Puede seguirse cualquier orden, pero deben hacerse los tres. En este caso, comenzaremos siempre por definir las URLs.

<br/>

Una plantilla de URL describe la forma en la que la URL está estructurada. Además, también le indica a Django qué debe buscar cuando recibe una solicitud.

Cada una de estas URLs se mapea a una *vista*, una función que recibe y devuelve la información necesaria para esa página. La función normalmente muestra la página siguiendo una plantilla, la cual contiene la estructura de la página web.

Por ahora, comenzaremos creando la página de inicio de la aplicación para poner en práctica estos tres pasos.


<br/><hr/><br/>


## Mapear una URL

Los usuarios hacen peticiones de páginas a través de URLs. La página principal será la que tenga la URL base de la aplicación, que en este momento es: `http://localhost:8000/`, la cual muestra una página por defecto de Django.

Vamos a cambiar esto. Para empezar, accederemos al archivo `urls.py` situado dentro de `learning_log`. Este es el código que deberías ver:

```python
# urls.py

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

<br/>

Las primeras dos líneas importan los módulos necesarios para el sitio admin. La lista `urlpatterns` define las URLs de la aplicación, y dentro de esta lista encontramos `admin.site.urls`, que define las URLs del sitio admin.

Debemos incluir las URLs de `learning_logs`, así que añadimos lo siguiente:

```python
# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
]
```

<br/>

Con esta modificación, hemos añadido el módulo `include`. Después, hemos indicado que añada en la lista `urlpatterns` las URLs de la aplicación `learning_logs`, ubicadas en el módulo `urls.py` (*que aún no hemos creado*).

Vamos a crear el archivo `urls.py` dentro de `learning_logs` y añadimos el siguiente código:

```python
# learning_logs/urls.py

""" Defines URL patterns for learning_logs. """

from django.urls import path

from . import views


app_name = "learning_logs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
]
```

<br/>

1. Hemos importado el módulo `path` que es necesario para mapear las URLs a las *vistas*. También hemos importado el módulo `views` de la aplicación `learning_logs`.
    > El punto inicial le dice a Python que busque el módulo `views.py` en el mismo directorio en el que se encuentra el propio archivo `urls.py`.
2. La variable `app_name` ayuda a Django a distinguir este archivo `urls.py` de los archivos `urls.py` de otras aplicaciones. En este caso, la aplicación se llama `learning_logs`, por lo que el valor de `app_name` es `"learning_logs"`.
3. La variable `urlpatterns` es una lista de páginas individuales que se pueden solicitar a la aplicación.

<br/>

La plantilla de URL para la página principal es una llamada a `path()` que incluye tres argumentos:

1. Una cadena que permite a Django mostrar la página correcta. Se ignora la parte de la URL que coincide con la URL base del proyecto, `http://localhost:8000/`, por ello hemos dejado la cadena vacía, para que la URL de la página principal coincida con la URL base.
2. La función que se llama cuando se solicita la página. En este caso, la función `index()` de `views.py` (*escribiremos esta vista en el siguiente apartado*).
3. El nombre de la plantilla de la URL, que nos permite referirnos a ella en otras partes del código. En este caso, el nombre es `"index"`.


<br/><hr/><br/>


## Escribir una vista

La función de una vista toma información de la petición del usuario, prepara los datos necesarios para generar una página y envía esos datos al navegador, muchas veces, haciendo uso de una plantilla.

El archivo `views.py` de `learning_logs` se generó automáticamente cuando ejecutamos `python manage.py startapp`. Abre este archivo y modifica el contenido de la siguiente manera:

```python
# views.py

from django.shortcuts import render

# Create your views here.
def index(request):
    """ The home page for Learning Log. """

    return render(request, "learning_logs/index.html")
```

<br/>

Cuando una petición de URL coincide con un patrón de URL que hemos definido en `urls.py`, Django llama a la función `index()` de `views.py`. Entonces, Django pasa un objeto `request` a la vista.

En este caso, no tenemos que manipular ningún dato, así que dentro de la función solo tendremos que llamar a `render()`. Esta función `render()` recibe dos parámetros:

1. El objeto `request` original.
2. La plantilla que se va a utilizar para construir la página.


<br/><hr/><br/>


## Escribir una plantilla

Las plantillas definen cómo se va a ver la página web, y Django las rellena con la información necesaria cada vez que se solicita la página. Las plantillas permiten acceder a los datos proporcionados por las vistas.

> Como nuestra página de inicio no requiere de datos, la plantilla va a ser muy simple.

<br/>

* Dentro de la carpeta `learning_logs`, crea una nueva carpeta llamada `templates`.
* Dentro de esta nueva carpeta, crea una nueva carpeta llamada `learning_logs`.
* Dentro de esta nueva carpeta, crea un archivo llamado `index.html`.

> `learning_logs/templates/learning_logs/index.html`
>
> Esta puede resultar una estructura demasiado redundante, sin embargo, es muy útil trabajar de esta forma, debido a que en ocasiones se crean varias aplicaciones que finalmente forman una sola dentro de un mismo proyecto. En este caso, nuestra aplicación está formada por una única aplicación, pero es una buena práctica seguir esta estructura.

<br/>

Dentro del archivo `index.html`, añade el siguiente código:
    
```html
<p>Learning Log</p>

<p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
```

<br/>

> Las etiquetas `<p>` son etiquetas de párrafo (teniendo las *versiones* de apertura `<p>`, y de cierre `</p>`), donde el contenido mostrado entre las etiquetas de apertura y cierre forma un nuevo párrafo.

<br/>

Ahora, ejecutamos el servidor y abrimos el navegador en la dirección `http://localhost:8000/`. Veremos la página de inicio de nuestra aplicación.

> Para ejecutar la aplicación, si no lo estuviera ya, se debe usar el siguiente comando:
>
> ```python
> python manage.py runserver
> ```

<br/>

Al haber realizado una petición a la URL base de la aplicación, Django ha buscado un patrón de URL que coincida con la URL base (coincide en el patrón `""`). Entonces, Django llama a `views.index()`, función que renderizará la página a través de la plantilla `index.html`.

Puede parecer un proceso largo y complicado para crear simplemente una vista, pero este proceso nos permite crear aplicaciones web complejas de forma sencilla y eficiente, separando las URL, las vistas y las plantillas. En proyectos más grandes, esto permite separar el trabajo entre varios aspectos de la aplicación.


<br/><hr/>
<hr/><br/>

<div align='right'>
    <a href="#index">Volver arriba</a>
</div>

# Escribir páginas adicionales

Ahora que hemos establecido una ruta para crear una página, podemos comenzar a crear el proyecto Learning Log. Vamos a crear dos páginas para mostrar datos:

1. Una página que muestre todos los temas.
2. Una página que muestre todas las entradas de un tema en particular.

<br/>

Para cada una de las páginas, especificaremos un patrón de URL, escribiremos una función de vista y crearemos una plantilla.

Antes de hacer esto, crearemos una plantilla base de la cual todas las demás plantillas del proyecto puedan heredar.


<br/><hr/><br/>


## Herencia de plantillas

Al crear una aplicación web, existen elementos que serán requeridos continuamente, y se repetirán en todas las páginas. En lugar de crear esos elementos en todas las plantillas, podemos escribir una plantilla base de la que hereden las demás.

Esto permite focalizarse en el contenido individual de cada una de las páginas.


<br/><br/>


### La plantilla base

Crearemos una plantilla llamada `base.html` en el mismo directorio que creamos `index.html`.

> `learning_logs/templates/learning_logs/base.html`

<br/>

Dentro de esta nueva plantilla, añadimos el siguiente código:

```html
<!-- base.html -->

<!-- 1 -->
<p>
    <a href="{% url 'learning_logs:index' %}">Learning Log</a>
<p>

<!-- 2 -->
{% block content %}{% endblock content %}
```

<br/>

1. Hemos creado un párrafo que contiene el nombre del proyecto, el cual también actúa como una especie de enlace a la página principal. Para generar el link, a parte de usar la etiqueta de link `<a>`, hemos usado usado un *template tag* de Django, el cual se indica con `{% %}`. En este caso, el *template tag* es `url`, y le hemos pasado como argumento el nombre de la plantilla de la URL, que en este caso es `learning_logs:index`. Esto genera una URL que coincide con el patrón de URL definido en `learning_logs/urls.py` con el nombre `index`. `learning_logs` actúa como un *namespace* e `index` sería el nombre propio de la URL de ese *namespace*. El valor del *namespace* viene dado por la variable `app_name` que definimos en `learning_logs/urls.py`.

2. Hemos insertado un par de etiquetas de bloque. Este bloque, llamado `content`, es un *placeholder*, la plantilla **hija** que herede de esta plantilla base, definirá el contenido dentro de esta *template tag*.

> Una plantilla hija no tiene por qué definir tantos bloques como tenga la plantilla base, puede definir menos, en cuyo caso hará uso sólo de aquellos que necesite.


<br/><br/>


### La plantilla hija

Vamos a aprovechar la plantilla creada en apartados anteriores llamada `index.html` para hacer que herede de la plantilla base que acabamos de crear.

Para ello, abrimos el archivo `index.html` y lo modificamos de la siguiente manera:

```html
<!-- index.html -->

{% extends "learning_logs/base.html" %}

{% block content %}
    <p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
{% endblock content %}
```

<br/>

Como habrás podido deducir, hemos sustituido el párrafo original que contenía el nombre de la aplicación, por aquello que hemos añadido en la plantilla `base.html`, que es el enlace a la página de inicio.

Hemos definido el contenido del bloque `content` con el párrafo que teníamos originalmente en `index.html`, y después, hemos indicado dónde termina dicho bloque.

> La etiqueta {% endblock %} no necesita de ningún nombre, pero es una buena práctica añadirlo para que sea más sencillo leer y organizar el código, sobre todo cuando el número de bloques es mayor.


<br/><hr/><br/>


## Página de temas

Ahora que hemos creado una plantilla base, podemos crear nuestras siguientes dos páginas (*como ya hemos mencionado anteriormente*):

1. Una página que muestre todos los temas.
2. Una página que muestre todas las entradas de un tema en particular.

<br/>

Comenzaremos por la primera, la página de temas.


<br/><br/>


### Patrón de URL para los temas

Comenzaremos definiendo la URL para la página de temas. Normalmente, se suelen utilizar URLs que describan lo que va a mostrarse en dicha página. En nuestro caso, la URL que usaremos será `http://localhost:8000/topics/`.

Vamos a modificar el archivo `learning_logs/urls.py` de la siguiente manera:

```python
# learning_logs/urls.py

# ...

urlpatterns = [
    # Home page
    # ...
    # Page that shows all topics
    path("topics/", views.topics, name="topics"),
]
```

<br/>

Hemos añadido un nuevo patrón de URL que coincide con la URL `http://localhost:8000/topics/`. El nombre de la plantilla de la URL es `"topics"`, y la función de vista que se llama es `views.topics()`.


<br/><br/>


### La vista de los temas

La función de vista `topics()` debe obtener los datos necesarios de la base de datos y enviarlos a la plantilla. Para ello, abrimos el archivo `views.py` y añadimos el siguiente código:

```python
# views.py

# ...
from .models import Topic


# Create your views here.
def index(request):
    # ...


def topics(request):
    """ Show all topics. """

    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)
```

<br/>

En primer lugar, hemos importado el modelo `Topic` asociado a los datos que necesitamos. La función `topics()` necesita un parámetro: el objeto `request` que Django recibe del servidor.

A continuación, realizamos una petición a la base de datos para obtener los objetos de tipo `Topic`, ordenados por la fecha de creación. El resultado de esta petición lo almacenamos en la variable `topics`.

Definimos el contexto que será enviado a la plantilla. Un *contexto* es un diccionario en el que las claves son los nombres que se usarán en la plantilla para acceder a los datos, y los valores son los datos que se enviarán a la misma.

Finalmente, llamamos a `render()` y le pasamos el objeto `request`, la ruta a la plantilla y el contexto.


<br/><br/>


### La plantilla de los temas

La plantilla para los temas recibe el diccionario `context`, de esta forma, puede acceder a los datos que le aporta la función de vista `topics()`.

Crea un archivo llamado `topics.html` dentro de la carpeta `learning_logs/templates/learning_logs/` y añade el siguiente código:

```html
<!-- topics.html -->

{% extends "learning_logs/base.html" %}

{% block content %}
    
    <p>Topics</p>

    <ul>
        {% for topic in topics %}
            <li>{{ topic }}</li>
        {% empty %}
            <li>No topics have been added yet.</li>
        {% endfor %}
    </ul>

{% endblock content %}
```

<br/>

Como hemos visto en [apartados anteriores](#herencia-de-plantillas), hemos usado la etiqueta `{% extends %}` para heredar de la plantilla base, y hemos definido el contenido del bloque `content`.

El contenido de esta plantilla contiene una lista de temas, que se genera a través de un bucle `for` que recorre el diccionario `context` y muestra cada uno de los temas. En este caso, como no se trata de código Python, se debe utilizar la etiqueta `{% endfor %}` para indicar el fin de un bucle `for`.

La etiqueta `{% empty %}` se usa para mostrar un mensaje cuando no hay ningún tema en la base de datos.

Ahora, vamos a modificar la plantilla base para que muestre un enlace a la página de temas. Abre el archivo `base.html` y modifica el código para que quede de la siguiente manera:

```html
<!-- base.html -->

<p>
    <a href="{% url 'learning_logs:index' %}">Learning Log</a> - 
    <a href="{% url 'learnign_logs:topics' %}">Topics</a>
</p>

{% block content %}{% endblock content %}
```

<br/>

Hemos añadido un ` - ` al final del primer enlace para separar los dos enlaces. A continuación, hemos añadido un enlace a la página de temas, y hemos usado el *template tag* `url` para generar la URL correcta.

Si accedemos a la web en el navegador y hacemos clic en el enlace `Topics` (*o escribimos `localhost:8000/topics/`*), veremos que se muestra la página de temas, y si no hay ningún tema en la base de datos, se mostrará el mensaje `No topics have been added yet.`.


<br/><hr/><br/>


## Páginas de temas individuales

Ahora que hemos creado la página de temas, vamos a crear la página de temas individuales. Estas páginas mostrarán el nombre del tema y todas las entradas asociadas a ese tema en particular.


<br/><br/>


### Patrón de URL para los temas individuales

Este patrón de URL va a ser ligeramente diferente a los vistos hasta ahora, y es que vamos a usar el `id` de cada tema para generar la URL. De esta forma, la URL para el tema `Chess` (*cuyo `id` es `1`*) será `http://localhost:8000/topics/1/`.

He aquí el código que debes situar en `learning_logs/urls.py`:

```python
# urls.py

# ...

urlpatterns = [
    # Home page
    # ...
    # Page that shows all topics
    # ...
    # Detail page for a single topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
```

<br/>

La cadena de texto `topics/<int:topic_id>` dice a Django lo siguiente:

1. **`topics`:** Es la primera parte de la cadena y dice a Django que busque URLs que tengan la palabra *topics* después de la base de la URL.
2. **`/<int:topic_id>`:** Busca un tipo de dato entero y almacena el entero en un argumento llamado `topic_id`.

<br/>

Cuando Django encuentra una URL que coincide con este patrón, llama a la función de vista `topic()` con el valor almacenado en `topic_id` como argumento. Utilizaremos este valor para obtener el tema correcto dentro de la función.


<br/><br/>


### La vista de los temas individuales

Hemos dicho anteriormente que la función `topic()` debe obtener como argumento el `topic_id` y obtener la información de dicho tema. Para ello, crearemos la siguiente función:

```python
# views.py

# ...

def topic(request, topic_id):
    """ Show a single topic and all its entries. """

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {
        "topic": topic,
        "entries": entries
    }
    return render(request, "learning_logs/topic.html", context)
```

<br/>

En este caso, la función no solo recibe el objeto `request`, sino que debe obtener el valor del `id` almacenado en `topic_id` como parámetro, valor obtenido dentro de la URL como `<int:topic_id>`.

A continuación, hacemos uso de `get()` para obtener el tema en base al ID.

Después de esto, obtenemos las entradas referidas a esos temas ordenadas en función de la fecha. Se coloca el signo negativo, `-`, para indicar que sea en sentido reverso, es decir, que se muestren primero las entradas más recientes.

Finalmente, se genera el contexto, añadiendo el tema y las entradas del mismo, y se llama a la función `render()` con el objeto `request`, la ruta a la vista y el contexto como parámetros.


<br/><br/>


### La plantilla de los temas individuales

En primer lugar, crearemos el archivo `topic.html` en la ruta `learning_logs/templates/learning_logs/` y añadiremos el siguiente código en el archivo:

```html
<!-- topic.html -->

{% extends 'learning_logs/base.html' %}

{% block content %}

<p>Topic: {{ topic }}</p>

<p>Entries:</p>
<ul>
    {% for entry in entries %}
        <li>
            <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
            <p>{{ entry.text|linebreaks }}</p>
        </li>
    {% empty %}
        <li>There are no entries for this topic yet.</li>
    {% endfor %}
</ul>

{% endblock content %}
```

<br/>

En el primer párrafo hemos añadido la palabra *Topic* y, después de los dos puntos, hemos añadido el valor almacenado en `topic` dentro del contexto, el cual es el propio nombre del tema seleccionado.

Después, hemos añadido un segundo párrafo que dice *Entries*, al cual sigue una lista de las entradas almacenadas en `entries` dentro del contexto. Se genera un ítem nuevo en la lista gracias al bucle `for` que se ha definido. Además, si no existen entradas aún, se muestra el mensaje `There are no entries for this topic yet.`.

En caso de existir entradas, se muestran:

1. La información referente a la fecha de creación de la misma a la que se ha aplicado el siguiente filtro (*en Django se insertan filtros usando `|`*): `M d, Y H:i`. Este filtro implica que se va a mostrar la fecha con el siguiente formato: `January 1, 2024, 22:13`.
2. El texto contenido en la propia entrada. A este texto también se le ha aplicado un filtro (`linebreaks`), el cual se asegura de que muestre el texto con saltos de línea adecuados para mostrar el contenido en la web, en lugar de mostrarlo todo en una sola línea.


<br/><br/>


### Links para las páginas de temas individuales

Antes de observar cómo se ve cada tema individual en la página web, comenzaremos modificando el archivo `topics.html` para asegurarnos de que se muestra el tema correcto al hacer click en los temas de la lista:

```html
<!-- topics.html -->

<!-- ... -->

<ul>
    {% for topic in topics %}
        <li>
            <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
        </li>
    {% empty %}
    <!-- ... -->
</ul>

<!-- ... -->
```

<br/>

Con esta modificación, hemos conseguido que al mostrarse la página con todos los temas, éstos sean realmente enlaces que puedan llevar al usuario a las páginas individuales de los mismos.

Esto se consigue indicando que la URL está basada en el patrón `topic` de `learning_logs`, y como requiere de un `topic_id` como argumento, le añadimos el `topic.id` al final.

Si refrescas la web, verás cómo te permite navegar entre los diferentes temas.


<br/><hr/>
<hr/><br/>


# Cuentas de usuario

*Próximamente...*