# Testear clases

Testear una clase es similar a testear funciones. Una posible diferencia es que en vez de pasarle argumentos a una función, se crean instancias de la clase y se les pasan argumentos a sus métodos.

<br>

Vamos a crear una clase para testearla. La clase se llama `AnonymousSurvey`, servirá para hacer encuestas de forma anónima y contará con 4 métodos:

* `__init__`: recibe una pregunta y crea un atributo `self.question` con el valor de la pregunta. También crea un atributo `self.responses` que es una lista vacía, donde se guardarán las respuestas.

* `show_question`: muestra la pregunta.

* `store_response`: recibe una respuesta y la guarda en la lista `self.responses`.

* `show_results`: muestra todas las respuestas.

<br>

He aquí el código de la clase:

```python
# survey.py

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

<br>

Una vez creada la clase, vamos a crear un archivo llamado `language_survey.py` que usará la clase creada para realizar una encuesta. El código del archivo es el siguiente:

```python
# language_survey.py

from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

<br>

Esta clase funcionará para una simple encuesta que reciba una única respuesta cada vez.


<br><hr>
<hr><br>


## Testear la clase

Para testear la clase, vamos a crear un archivo llamado `test_survey.py`.

En este archivo, importaremos la clase `AnonymousSurvey` y la clase `unittest.TestCase` de la librería `unittest`. Luego, crearemos una clase llamada `TestAnonymousSurvey` que heredará de `unittest.TestCase`.

Dentro de esta clase, crearemos un método llamado `test_store_single_response` que creará una instancia de la clase `AnonymousSurvey` y le pasará una respuesta. Luego, comprobaremos que la respuesta se haya guardado correctamente.

He aquí el código del archivo:

```python
# test_survey.py

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

<br>

Si ejecutamos el archivo, obtenemos el siguiente resultado:

```bash
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

<br>

Ahora surge otra pregunta: *¿funciona esta clase para aquellos casos en los que la clase reciba más de una respuesta a la vez?*

Vamos a crear otro método para comprobarlo:

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    # nuevo método añadido
    def test_store_multiple_responses(self):
        """ Test that multiple responses are stored properly. """
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["English", "Spanish", "Euskera"]
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

<br>

Si ejecutamos esta vez el archivo `test_survey.py` obtenemos lo siguiente:

```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```


<br><hr>
<hr><br>


## El método setUp()

Hemos visto que para testear las clases, es necesario crear instancias de las mismas cada vez que se quieran testear, es decir, dentro de cada módulo de testing hay que realizar una instancia de la clase. **Esto puede ser algo muy tedioso y repetitivo**.

Por ello, `unittest.TestCase` proporciona el método `setUp()`. Si se añade este método, éste se ejecuta justo antes de comenzar a ejecutar los demás métodos que comienzan por `test_`. Esto nos permite crear objetos en el método `setUp()` y utilizar dicho objeto en el resto de los métodos `test_`.

Añadámoslo en la clase `TestAnonymousSurvey`:

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    def setUp(self):
        """ Create a survey and a set of responses for use in all test methods. """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Euskera"]

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])

        self.assertIn('English', self.my_survey.responses)

    def test_store_multiple_responses(self):
        """ Test that multiple responses are stored properly. """
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

<br>

Como se puede observar, en el método `setUp()` se añaden aquellos elementos ***globales*** a usar en los demás métodos, por lo que se pueden modificar dichos métodos de testing para no tener que crear instancias, ni respuestas para comparar resultados, y acceder a esos valores globales definidos en `setUp()` mediante `self`.

<br>

Si ejecutamos de nuevo el archivo, obtenemos lo siguiente:

```bash
..
----------------------------------------------------------------------    
Ran 2 tests in 0.000s

OK
```