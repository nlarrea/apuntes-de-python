# ALIEN INVASION

<br/><hr/>
<hr/><br/>

# Antes de comenzar

En esta ocasión vamos a crear el más que conocido *'juego de los alienígenas'*.

Antes de comenzar a descargar paquetes, se va a hacer uso de un entorno virtual mediante `pipenv` para evitar posibles problemas posteriores, así como la instalación de *demasiados* recursos.

<br/>

Por ello, en primer lugar y desde el directorio actual en la terminal, se ejecuta lo siguiente:

```bash
pipenv --python 3.10.7
```

<br/>

De esta forma, se trabajará con esa versión de Python y se instalarán aquí únicamente aquellos paquetes necesarios para llevar a cabo este proyecto.


<br/><hr/><br/>


## Descripción del proyecto

El proyecto consiste en crear un videojuego. En él, el usuario controlará una nave espacial que se moverá de forma horizontal en la parte inferior de la pantalla haciendo uso de las flechas de dirección. A su vez, al pusar la tecla de espacio, la nave disparará balas.

Cuando el juego comienza, una flota alienígena que se va moviendo por la pantalla aparece. El jugador debe disparar para destruir a los alienígenas.

Si el jugador destruye a todos los enemigos, una nueva flota aparece, una que se mueva más rápido. Si algún alien toca al jugador o llega a la parte inferior de la pantalla, el jugador pierde una nave. Si el jugador pierde tres naves, el juego termina.


<br/><hr/><br/>


## Intalación de Pygame

Antes de comenzar a crear el programa, es necesario instalar `Pygame`, un paquete que permitirá trabajar de forma mucho más sencilla a lo largo de este proyecto.

Como hemos decidido usar `pipenv`, debemos ejecutar el siguiente comando desde el directorio de trabajo:

```bash
pipenv install pygame
```

<br/>

> Si no se estuviera usando `pipenv`:
>
> ```bash
> python -m pip install --user pygame
> ```


<br/><hr/>
<hr/><br/>


# Creación del proyecto

Vamos a comenzar a crear el programa creando una ventana vacía de Pygame. Después, dibujaremos los elementos (*las naves, los aliens, etc.*).

Además, también será necesario crear código para poder leer la entrada del usuario.


<br/><hr/><br/>


## Crear la ventana de Pygame y responder a la entrada de usuario

Vamos a crear el archivo del proyecto (`alien_invasion.py`), y en ella vamos a crear el siguiente código:

```python
# alien_invasion.py

import sys
import pygame

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

<br/>

En primer lugar, se importan los módulos `sys` y `pygame`. El módulo `sys` se usará para salir del juego cuando el usuario haga clic en el botón de cerrar. El módulo `pygame` contiene las funcionalidades necesarias para crear un juego.

<br/>

A continuación, se crea la clase `AlienInvasion`. Esta clase representa el juego en sí. En el método `__init__()` se inicializan los recursos del juego. En este caso, se inicializa el fondo de la pantalla y se crea una instancia de `pygame.display`.

<br/>

El método `run_game()` contiene un bucle `while` que contiene un bucle `for` para detectar los eventos del teclado y del ratón. El bucle `while` se ejecuta continuamente para mantener la ventana del juego abierta. El bucle `for` se ejecuta cada vez que el usuario realiza una acción, como pulsar una tecla o mover el ratón. El bucle `for` contiene una serie de declaraciones `if` para detectar eventos específicos y realizar las acciones apropiadas, en nuestro caso, por ahora solo hemos creado una acción: salir del juego.

La llamada a `pygame.display.flip()` actualiza la pantalla con cada ejecución del bucle `while` y dibuja una pantalla vacía en cada pasada del bucle, borrando la pantalla anterior para mostrar la nueva.

<br/>

Por último, se crea una instancia de `AlienInvasion` y se llama al método `run_game()` para ejecutar el juego.


<br/><hr/><br/>


## Crear un fondo para el juego

Por defecto, Pygame genera una pantalla de color negro. Vamos a configurar esto para colocar el color que deseemos, lo haremos dentro del método `__init__()`:

```python
# alien_invasion.py

import sys
import pygame

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

<br/>

Los colores en Pygame se especifican en formato RGB. En este caso, se ha elegido un gris claro para el fondo, concretamente el color `(230, 230, 230)`.

Se ha asignado este color a `self.bg_color` y se ha usado para llenar la pantalla en cada pasada del bucle `while`.


<br/><hr/><br/>


## Crear una clase 'Settings'

Cada vez que introduzcamos nuevas funcionalidades al programa, vamos a necesitar generar una serie de configuraciones.

Con el objetivo principal de mantener dichas configuraciones en un único lugar, vamos a crear una clase llamada `Settings` dentro de un nuevo archivo, al que llamaremos `settings.py`. De esta forma, si necesitamos cambiar alguna configuración, solo tendremos que modificar el archivo `settings.py` en lugar de tener que buscar en todo el código.

<br/>

He aquí el código de la clase `Settings`:

```python
# settings.py

class Settings:
    """ A class to store all settings for Alien Invasion. """

    def __init__(self):
        """ Initialize the game's settings. """
        # screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
```

<br/>

Ahora, para crear una instancia de la clase `Settings` y usarla en `alien_invasion.py`, debemos importarla y modificar el código del archivo de tal forma que las configuraciones especificadas en la clase sustituyan a las que teníamos anteriormente:

```python
# alien_invasion.py

import sys
import pygame

from settings import Settings

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

<br/>

Los cambios realizados son los siguientes:

* Se ha importado la clase `Settings` desde el módulo `settings`.
* Se ha creado una instancia de `Settings` en `__init__()`.
* Se han sustituido los valores hardcodeados en `pygame.display.set_mode()` por las variables `self.settings.screen_width` y `self.settings.screen_height`.
* Se ha eliminado el color de fondo definido en `__init__()` y se ha utilizado el valor de `self.settings.bg_color`.

<br/>

Si ejecutamos los cambios (*recordatorio: estamos usando `pipenv`*), veremos que el juego sigue funcionando exactamente igual que antes, pero ahora tenemos una clase `Settings` que podemos usar para almacenar todas las configuraciones del juego.


<br/><hr/><br/>


## Crear la nave espacial

### Seleccionar una imagen

Se pueden utilizar prácticamente imágenes de cualquier formato, sin embargo, el formato más sencillo con el que trabajar en este caso será con los archivos bitmap (`.bmp`), puesto que Pygame carga las imágenes en este formato por defecto.

<br/>

Vamos a acceder a cualquier página que nos permita descargar imágenes para utilizarlas en nuestros proyectos o a crear la nuestra propia.

En este caso, la imagen seleccionada para utilizarla como nave espacial en nuestro videojuego es la siguiente:

![ship](./images/ship.bmp)


<br/><br/>


### Crear una clase 'Ship'

Después de seleccionar la nave, tenemos que hacer que aparezca en la pantalla. Para ello, vamos a crear una clase en otro archivo llamado `ship.py`, donde definiremos todos los aspectos de la nave espacial que manejará el jugador.

He aquí el código escrito en dicho archivo:

```python
# ship.py

import pygame

class Ship:
    """ A class to manage the ship. """

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the botom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
```

<br/>

Una gran ventaja de Pygame es que permite tratar a todos los elementos del juego como si fueran rectángulos (`rect`), lo que facilita muchísimo la geometría.

<br/>

En primer lugar, se importa la librería correspondiente (`pygame`) para poder trabajar, y, a continuación, se genera la clase `Ship` que definirá nuestra nave espacial.

El método `__init__()` recibe dos parámetros:

* La referencia `self`
* La referencia a la instancia actual de la clase `AlienInvasion`.

<br/>

Con el objetivo de facilitar el acceso a la pantalla del juego, creamos un atributo `self.screen`. Como vamos a trabajar con *rectángulos*, obtenemos el rectángulo de la ventana de juego con `ai_game.screen.get_rect()`.

Para cargar la imagen de la nave usamos `pygame.image.load()`, a continuación, usamos `get_rect()` para acceder al atributo `rect` de la imagen y, finalmente, establecemos la posición de la nave en la parte inferior central de la pantalla.

<br/>

Finalmente, creamos el método `blitme()` que dibuja la imagen de la nave en la pantalla en la posición especificada por `self.rect`.


<br/><br/>


### Mostrar la nave en la pantalla

Para mostrar la nave en la pantalla, tenemos que modificar el archivo `alien_invasion.py` de la siguiente forma:

```python
# alien_invasion.py

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # to draw the ship
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

<br/>

Los cambios realizados son los siguientes:

* Se ha importado la clase `Ship` desde el módulo `ship`.
* Se ha creado una instancia de `Ship` en `__init__()`.
* Se ha añadido el método `self.ship.blitme()` en el bucle `while` para dibujar la nave en la pantalla.


<br/><hr/><br/>


## Refactorizar métodos

### Refactorizar check_events()

En proyectos largos, suele ser habitual refactorizar el código para que este sea más fácil de mantener.

En este caso, vamos a refactorizar el método `run_game()`, creando otros métodos auxiliares. Los métodos auxiliares son aquellos que no tienen que llamarse desde fuera de la clase, por lo que se nombran con un guión bajo al principio del nombre, creando así métodos privados.

<br/>

El archivo `alien_invasion.py` queda de la siguiente manera tras modificar el método `run_game()` quedará de la siguiente forma:

```python
# alien_invasion.py

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # to draw the ship
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

<br/>

Como se puede observar, se ha creado el método `_check_events()` que se encarga de gestionar los eventos de teclado y ratón. Además, se ha eliminado el bucle `for` del método `run_game()` y se ha añadido la llamada al método `_check_events()`. Ahora, para ejecutar esa función, se llama a `self._check_events()` desde el método `run_game()`.


<br/><br/>


### Refactorizar update_screen()

De la misma forma que hemos refactorizado el método `run_game()` añadiendo el método `_check_events()`, vamos a refactorizar el método `run_game()` añadiendo el método `_update_screen()`.

Este nuevo método se encargará de actualizar la pantalla en cada iteración del bucle `while`, haciendo que el código sea más fácil de leer.

<br/>

El archivo `alien_invasion.py` queda de la siguiente manera tras modificar el método `run_game()` quedará de la siguiente forma:

```python
# alien_invasion.py

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            # Redraw the screen during each pass through the loop.
            self._update_screen()
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
         """ Update images on the screen, and flip to the new screen. """
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

<br/>

Hemos movido el código que se encarga de actualizar la pantalla al método `_update_screen()`, y hemos llamado a este método desde el método `run_game()`.

<br/>

Ahora que hemos reestructurado el código, podemos enfocarnos en la parte de la lógica del juego.


<br/><hr/><br/>


## Movimiento de la nave

En la descripción del proyecto, hemos indicado que el usuario sería capaz de mover la nave hacia la derecha e izquierda.

En este apartado, vamos a añadir el código necesario para que el usuario pueda mover la nave pueda realizar dichos movimientos.


<br/><br/>


### Respondiendo a eventos de teclado

Pygame detecta y registra como un evento las acciones del usuario, como pulsar una tecla o mover el ratón. Para ello, se hace uso del método `pygame.event.get()`.

En nuestro programa, debemos modificar el método `_check_events()` para que detecte los eventos de teclado. Cuando Pygame detecte un evento de estos, debemos tener en cuenta si la tecla pulsada tiene una acción asociada. En caso de que la tenga, debemos realizar la acción correspondiente.

<br/>

En nuestro caso, las teclas que debemos tener en cuenta para el movimiento de la nave son la `flecha derecha` y la `flecha izquierda`.

<br/>

Vamos a modificar el método `_check_events()` para que detecte los eventos de teclado y realice las acciones correspondientes.

```python
# alien_invasion.py

# class AlienInvasion
def _check_events(self):
    """ Respond to keypresses and mouse events. """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right.
                        self.ship.rect.x += 1
```

<br/>

En este caso, hemos añadido un nuevo bloque `elif` que se encarga de detectar si el evento es de tipo `pygame.KEYDOWN`, es decir, si se ha pulsado una tecla.

En caso de que se haya pulsado una tecla, se comprueba si la tecla pulsada es la `flecha derecha` (`pygame.K_RIGHT`). Si la tecla pulsada es la `flecha derecha`, se mueve la nave un píxel a la derecha.

<br/>

Esto puede ser un movimiento poco fluido, por lo que vamos a tratar de permitir un movimiento más fluido de la nave.


<br/><br/>


### Movimiento continuo

Queremos conseguir que la nave se mueva de forma continua mientras se mantenga pulsada la tecla `flecha derecha`.

Vamos a aprovechar el evento `pygame.KEYDOWN` para detectar cuando se pulsa la tecla `flecha derecha`, y el evento `pygame.KEYUP` para detectar cuando se deja de pulsar la tecla `flecha derecha`.

<br/>

La clase `Ship` contiene todos los atributos de la nave, por lo que vamos a crear uno llamado `moving_right` que nos indique si la nave se está moviendo hacia la derecha o no, así como un método llamado `update()` que se encargue de actualizar la posición de la nave.

<br/>

Así queda la clase `Ship` tras añadir los nuevos atributos y métodos:

```python
# ship.py

import pygame

class Ship:
    """ A class to manage the ship. """

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the botom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False

    def update(self):
        """ Update the ship's position based on the movement flag. """
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
```

<br/>

Ahora, vamos a modificar el método `_check_events()` para que detecte cuando se pulsa la tecla `flecha derecha` y cuando se deja de pulsar.

```python
# alien_invasion.py

# class AlienInvasion
def _check_events(self):
    """ Respond to keypresses and mouse events. """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
```

<br/>

Finalmente, solo nos queda modificar el método `run_game()` para que llame al método `update()` de la nave en cada iteración del bucle principal.

```python
# alien_invasion.py

# class AlienInvasion
def run_game(self):
    """ Start the main loop for the game. """
    while True:
        # Watch for keyboard and mouse events.
        self._check_events()
        self.ship.update()

        # Redraw the screen during each pass through the loop.
        self._update_screen()
        
        # Make the most recently drawn screen visible
        pygame.display.flip()
```

<br/>

Ahora que hemos hecho esto para el movimiento hacia la derecha, vamos a hacer lo mismo para el movimiento hacia la izquierda.

Así es como quedaría el archivo `ship.py` tras añadir ambos movimientos:

```python
# ship.py

import pygame

class Ship:
    """ A class to manage the ship. """

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the botom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flags. """
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)
```

<br/>

Y así es como queda el archivo `alien_invasion.py` tras añadir ambos movimientos:

```python
# alien_invasion.py

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()

            # Redraw the screen during each pass through the loop.
            self._update_screen()
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                        

    def _update_screen(self):
         """ Update images on the screen, and flip to the new screen. """
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```


<br/><br/>


### Ajustar la velocidad de la nave

Ahora mismo, la nave se mueve un píxel por cada ciclo del bucle `while` del programa. Podemos ajustar esta velocidad añadiendo un atributo `ship_speed` a la clase `Settings`.

He aquí el código de la clase `Settings` tras añadir el atributo `ship_speed`:

```python
# settings.py

class Settings:
    """ A class to store all settings for Alien Invasion. """

    def __init__(self):
        """ Initialize the game's settings. """
        # screen settings
        # ...

        # ship settings
        self.ship_speed = 1.5
```

<br/>

Hemos añadido una velocidad de 1.5 píxeles, sin embargo, los atributos de `rect` solo admiten números enteros. Por ello, debemos realizar ciertas modificaciones a la nave:

```python
# ship.py

import pygame

class Ship:
    """ A class to manage the ship. """

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position. """
        # ...
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        # ...

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        # ...

    def update(self):
        """ Update the ship's position based on the movement flags. """
        # update the ship's x value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    # ...
```

<br/>

Lo que hemos hecho es crear un atributo `settings` para la nave, de esta forma, podríamos usarlo dentro del método `update()`. Como hemos modificado la velocidad a un tipo de dato decimal, debemos almacenar dicho valor en una variable que admita ese tipo de dato. Podemos asignar valores decimales a los atributos de `rect`, pero éste solo se quedará con la parte entera de dicho número.

Por ello, hemos creado el atributo `self.x` que almacenará el valor decimal de la posición horizontal de la nave. En el método `update()`, actualizamos el valor de `self.x` en lugar de `self.rect.x`, y después, actualizamos el valor de `self.rect.x` con el valor de `self.x`.


<br/><hr/><br/>


## Limitar el rango de movimiento de la nave

Ahora mismo, la nave es capaz de moverse fuera de la pantalla. Vamos a limitar el rango de movimiento de la nave para que no pueda salirse de la misma.

Para ello, moficaremos el método `update()` de la clase `Ship`:

```python
# ship.py

def update(self):
    """ Update the ship's position based on the movement flags. """
    # update the ship's x value, not the rect
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.x += self.settings.ship_speed
    if self.moving_left and self.rect.left > 0:
        self.x -= self.settings.ship_speed
    
    # ...
```

<br/>

Este código comprueba la posición actual de la nave antes de permitir el cambio de posición. Si la posición de la nave es menor que el ancho de la pantalla, se permite el movimiento hacia la derecha. Si la posición de la nave es mayor que 0, se permite el movimiento hacia la izquierda.


<br/><hr/><br/>


## Refactorizar _check_events()

A medida que la programación del juego vaya avanzando, el código de `_check_events()` se irá haciendo más largo. Por ello, vamos a refactorizarlo para que sea más fácil de leer.

Vamos a dividir el código de dicho método en otros dos:

```python
# alien_invasion.py

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    # ...

    def _check_events(self):
        """ Respond to keypresses and mouse events. """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # ...
```


<br/><hr/><br/>


## Pulsar 'Q' para salir del juego

Vamos a añadir la funcionalidad de que el usuario pueda salir del juego pulsando la tecla `Q`.

Para ello, vamos a modificar uno de los métodos que acabamos de crear: `_check_keydown_events()`.

```python
# alien_invasion.py

def _check_keydown_events(self, event):
    """ Respond to keypresses. """
    # ...
    elif event.key == pygame.K_q:
        sys.exit()
```


<br/><hr/><br/>


## Jugar a pantalla completa

Para permitir jugar en pantalla completa, se deben realizar las siguientes modificaciones en el constructor de la clase `AlienInvasion`:

```python
# alien_invasion.py

def __init__(self):
    """ Initialize the game, and create game resources. """
    # ...

    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height

    # ...
```


<br/><hr/><br/>


## Disparar

Vamos a añadir la funcionalidad de disparar a nuestro juego. Para ello, vamos a comenzar creando las propiedades `settings` necesarias de las `bullets`:

```python
# settings.py

class Settings:
    def __init__(self):
        # ...

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
```

<br/>

Ahora, vamos a crear la clase `Bullet`:

```python
# bullet.py

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship. """

    def __init__(self, ai_game):
        """ Create a bullet object at the ship's current position. """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)
```

<br/>

A continuación, vamos a crear los métodos `update()` y `draw_bullet()` de la clase `Bullet`:

```python
# bullet.py

class Bullet(Sprite):
    # ...

    def update(self):
        """ Move the bullet up the screen. """
        # update the decimal position of the bullet
        self.y -= self.settings.bullet_speed

        # update the rect position
        self.rect.y = self.y

    
    def draw_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)
```