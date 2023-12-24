# APLICACIONES WEB - Django

<div id="index" />

* [Primeros pasos con Django](#django)
* [Configurar el proyecto](#configurar-el-proyecto)
    * [Escribir una especificación](#escribir-una-especificación)
    * [Crear el entorno virtual](#crear-el-entorno-virtual)
    * [Instalar Django](#instalar-django)
* [Crear un proyecto de Django](#crear-un-proyecto-de-django)

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
> <br/>


<br/><hr/><br/>


## Instalar Django

Para instalar Django, con el **entorno virtual activado** ejecutamos el siguiente comando:

```bash
pip install django
```

<br/>

Esperamos a que se instale y listo, podremos usar Django en nuestro proyecto. Se ha de tener en cuenta que para poder utilizar Django, el entorno virtual ha de estar activado.


<br/><hr/>
<hr/><br/>

<div align='right'>
    <a href="#index">Volver arriba</a>
</div>

# Crear un proyecto de Django

