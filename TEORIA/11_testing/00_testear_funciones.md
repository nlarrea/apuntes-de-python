# Testear funciones

En ocasiones se crea cierto código con el que debemos comprobar si obtenemos la respuesta deseada para diferentes entradas posibles.

Esto es algo muy útil y recomendado en todos los casos.

Vamos a comenzar realizando una función que reciba un nombre y un apellido y de como resultado el nombre completo de la persona.

```python
# testear_funciones.py

def get_formated_name(first, last):
    """ Generate a neatly formated full name """
    full_name = f"{first} {last}"
    return full_name.title()
```

<br>

A continuación, vamos a comprobar que la función anterior funciona correctamente creando un bucle `while` para que el usuario pueda introducir los nombres que desee.

```python
# testear_funciones.py

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nEnter your first name: ")
    if first == "q": break

    last = input("Enter your last name: ")
    if last == "q": break

    formatted_name = get_formated_name(first, last)
    print(f"\nFormatted name: {formatted_name}")
```

<br>

Si llamamos a esta función con 2 parámetros (nombre y apellido), la función sí funciona, pero, ¿qué pasa si modificamos la función en algún momento? Tener que comprobar constantemente que la función en cuestión sigue funcionando puede ser algo muy tedioso.

Para ello, existen los tests.

Vamos a crear un archivo llamado '`test_name_function.py`'.


<br><hr>
<hr><br>


## Test unitario y caso de prueba

Dentro de este archivo, vamos a importar el módulo `unittest` y la función que queremos probar.

```python
import unittest
from testear_funciones import get_formated_name
```

<br>

Ahora, vamos a crear una clase. Esta clase contendrá los tests que queremos realizar, por lo que es necesario que herede de `unittest.TestCase`.

```python
class NamesTestCase(unittest.TestCase):
    """ Tests for 'testear_funciones.py' """

    def test_first_last_name(self):
        """ Do names like 'Janis Joplin' work? """
        formatted_name = get_formated_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

if __name__ == "__main__":
    unittest.main()
```

<br>

En este caso, hemos creado una clase llamada '`NamesTestCase`' que hereda de `unittest.TestCase`. Dentro de esta clase, hemos creado un método llamado '`test_first_last_name`' que contiene el código que queremos probar.

<br>

La variable '`formatted_name`' contiene el resultado de la función que queremos probar. A continuación, utilizamos el método '`assertEqual`'[^1] para comprobar que el resultado de la función es el que esperamos. Para ello, comparamos el resultado de la función con el resultado que sabemos que deberíamos obtener.

<br>

El '`if`' que se encuentra al final del archivo comprueba que el archivo se está ejecutando directamente. Si es así, se ejecuta el método '`main()`' de `unittest`. Este método busca todas las clases que heredan de '`unittest.TestCase`' y ejecuta todos los métodos que comiencen por '`test_`'.


<br><hr><br>


### Test que pasa (test positivo)

Tras ejecutar el archivo, obtenemos el siguiente resultado:

```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

<br>

El punto de la primera línea indica que se ha pasado un test. La siguiente línea indica que se ha ejecutado un test y muestra el tiempo aproximado que ha tardado en ejecutarse. La última línea indica que todos los tests han pasado.

Este output significa que la función que hemos probado funciona para todos los casos que sean iguales al que hemos probado, es decir, siempre que introduzcamos dos textos como parámetros, la función funcionará correctamente.


<br><hr><br>


### Test que falla

Para ver qué aspecto tiene un test fallido, vamos a modificar la función '`get_formated_name()`' para que no funcione correctamente.

```python
# testear_funciones.py

def get_formated_name(first, middle, last):
    """ Generate a neatly formated full name """
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

<br>

Hemos modificado la función de tal manera que necesite recibir 3 parámetros en vez de 2. Esto significa que el test que hemos creado anteriormente debería fallar.

Ahora, si ejecutamos el archivo '`test_name_function.py`', obtenemos el siguiente resultado:

```bash
E
======================================================================
ERROR: test_first_last_name (__main__.NamesTestCase)
Do names like 'Janis Joplin' work?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\Users\larre\Documents\NAIA\OpenBootcamp\4-Python\open-python\TEORIA\11_testing\test_name_function.py", line 11, in test_first_last_name
    formatted_name = get_formated_name("janis", "joplin")
TypeError: get_formated_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
```

<br>

En este caso, el '`E`' de la primera línea indica que un unit test ha fallado.

Las siguientes líneas indican que se ha producido un error en el test '`test_first_last_name`' de la clase '`NamesTestCase`'.

A continuación, se indica que se ha producido un error en la línea 11 del archivo '`test_name_function.py`'. Se especifica que la función '`get_formated_name()`' necesita recibir un parámetro más. Es el mismo formato que los errores comunes que se producen en Python.

La última línea indica que se ha producido un error y que el test ha fallado.


<br><hr><br>


### Responder ante un test fallido

Cuando un test falla, debemos tener en cuenta los mensajes recibidos, los cuales nos indican qué ha fallado y dónde la mayoría de las veces.

Sabiendo esto, es importante recordar que lo que se debe modificar es el código de la función, no el código del test.

<br>

En este caso, el error nos indica que la función '`get_formated_name()`' necesita recibir un parámetro más. Por lo tanto, debemos modificar la función para que funcione correctamente recibiendo tanto 2 como 3 parámetros.

```python
# testear_funciones.py

def get_formated_name(first, last, middle=""):
    """ Generate a neatly formated full name """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

<br>

Ahora, si ejecutamos el archivo '`test_name_function.py`', obtenemos el siguiente resultado:

```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```


<br><hr>
<hr><br>


## Añadir más tests

Ahora que sabemos que la función vuelve a funcionar para nombres con 2 parámetros, vamos a añadir más tests para comprobar que la función funciona correctamente para nombres con 3 parámetros.

Para ello, basta con añadir más métodos a la clase '`NamesTestCase`' que comiencen por '`test_`'.

La clase al completo quedaría así:

```python
class NamesTestCase(unittest.TestCase):
    """ Tests for 'testear_funciones.py' """

    def test_first_last_name(self):
        """ Do names like 'Janis Joplin' work? """
        formatted_name = get_formated_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_middle_last_name(self):
        """ Do names like 'Wolfgang Amadeus Mozart' work? """
        formatted_name = get_formated_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")
```

<br>

El resultado de ejecutar el archivo '`test_name_function.py`' sería el siguiente:

```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

<br>

Ahora sabemos que la función que hemos creado funciona tanto con dos como con tres parámetros.


<br><hr>
<hr><br>


## Métodos 'assert'

En los ejemplos vistos en este apartado hemos utilizado el método `asserEqual()`, que toma dos parámetros y comprueba si ambos parámetros son iguales. En caso de no ser así, lanza una excepción.

Sin embargo, existen varios métodos diferentes con los que poder trabajar pertenecientes también a `unittest.TestCase`.

He aquí una pequeña muestra de los más utilizados:

| **Métodos** | **Uso** |
| --- | --- |
| `assertEqual(a, b)` | Comprueba si: `a == b` |
| `assertNotEqual(a, b)` | Comprueba si: `a != b` |
| `assertTrue(x)` | Comprueba si: `x == True` |
| `assertFalse(x)` | Comprueba si: `x == False` |
| `assertIn(item, list)` | Comprueba si: `item` está dentro de `lista` |
| `assertNotIn(item, list)` | Comprueba si: `item` no está dentro de `lista` |


<br><hr>


[^1]: `assertEqual`' es un método que pertenece a la clase `unittest.TestCase`. Este método comprueba que el primer parámetro que le pasamos es igual al segundo parámetro que le pasamos. Si ambos parámetros son iguales, el test se pasa. Si no lo son, el test falla.