# ALIEN INVASION

<br><hr>
<hr><br>

# Antes de comenzar

En esta ocasión vamos a crear el más que conocido *'juego de los alienígenas'*.

Antes de comenzar a descargar paquetes, se va a hacer uso de un entorno virtual mediante `pipenv` para evitar posibles problemas posteriores, así como la instalación de *demasiados* recursos.

<br>

Por ello, en primer lugar y desde el directorio actual en la terminal, se ejecuta lo siguiente:

```bash
pipenv --python 3.10.7
```

<br>

De esta forma, se trabajará con esa versión de Python y se instalarán aquí únicamente aquellos paquetes necesarios para llevar a cabo este proyecto.


<br><hr><br>


## Descripción del proyecto

El proyecto consiste en crear un videojuego. En él, el usuario controlará una nave espacial que se moverá de forma horizontal en la parte inferior de la pantalla haciendo uso de las flechas de dirección. A su vez, al pusar la tecla de espacio, la nave disparará balas.

Cuando el juego comienza, una flota alienígena que se va moviendo por la pantalla aparece. El jugador debe disparar para destruir a los alienígenas.

Si el jugador destruye a todos los enemigos, una nueva flota aparece, una que se mueva más rápido. Si algún alien toca al jugador o llega a la parte inferior de la pantalla, el jugador pierde una nave. Si el jugador pierde tres naves, el juego termina.


<br><hr><br>


## Intalación de Pygame

Antes de comenzar a crear el programa, es necesario instalar `Pygame`, un paquete que permitirá trabajar de forma mucho más sencilla a lo largo de este proyecto.

Como hemos decidido usar `pipenv`, debemos ejecutar el siguiente comando desde el directorio de trabajo:

```bash
pipenv install pygame
```

<br>

> Si no se estuviera usando `pipenv`:
>
> ```bash
> python -m pip install --user pygame
> ```


<br><hr>
<hr><br>


# Creación del proyecto

Vamos a comenzar a crear el programa creando una ventana vacía de Pygame. Después, dibujaremos los elementos (*las naves, los aliens, etc.*).

Además, también será necesario crear código para poder leer la entrada del usuario.


<br><hr><br>


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

<br>

En primer lugar, se importan los módulos `sys` y `pygame`. El módulo `sys` se usará para salir del juego cuando el usuario haga clic en el botón de cerrar. El módulo `pygame` contiene las funcionalidades necesarias para crear un juego.

<br>

A continuación, se crea la clase `AlienInvasion`. Esta clase representa el juego en sí. En el método `__init__()` se inicializan los recursos del juego. En este caso, se inicializa el fondo de la pantalla y se crea una instancia de `pygame.display`.

<br>

El método `run_game()` contiene un bucle `while` que contiene un bucle `for` para detectar los eventos del teclado y del ratón. El bucle `while` se ejecuta continuamente para mantener la ventana del juego abierta. El bucle `for` se ejecuta cada vez que el usuario realiza una acción, como pulsar una tecla o mover el ratón. El bucle `for` contiene una serie de declaraciones `if` para detectar eventos específicos y realizar las acciones apropiadas, en nuestro caso, por ahora solo hemos creado una acción: salir del juego.

La llamada a `pygame.display.flip()` actualiza la pantalla con cada ejecución del bucle `while` y dibuja una pantalla vacía en cada pasada del bucle, borrando la pantalla anterior para mostrar la nueva.

<br>

Por último, se crea una instancia de `AlienInvasion` y se llama al método `run_game()` para ejecutar el juego.


<br><hr><br>


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

<br>

Los colores en Pygame se especifican en formato RGB. En este caso, se ha elegido un gris claro para el fondo, concretamente el color `(230, 230, 230)`.

Se ha asignado este color a `self.bg_color` y se ha usado para llenar la pantalla en cada pasada del bucle `while`.


<br><hr><br>


## Crear una clase 'Settings'

