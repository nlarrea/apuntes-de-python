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

*Próximamente...*