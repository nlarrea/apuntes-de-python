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