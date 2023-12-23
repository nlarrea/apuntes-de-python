# PROPIEDADES Y DECORADORES
"""
Crear atributos PROTEGIDOS: _
Crear atributos PRIVADOS: __
"""


class Invoice:
    def __init__(self, client, total) -> None:
        self._client = client       # Atributo protegido
        self._total = total         # Atributo protegido


    def formatter(self):
        return f"{self._client} owes: ${self._total}"
    
    """
    Al ser atributos protegidos, 'no podemos' acceder a ellos desde fuera de la
    clase, pero podemos usar decoradores para crear 'GETTERS' y 'SETTERS' para
    obtener y/o modificar los valores de los mismos.
    """

    # GETTER
    @property
    def client(self):
        return self._client
    

    # SETTER
    @client.setter
    def client(self, client):
        self._client = client

    
    # GETTER
    @property
    def total(self):
        return self._total
    
    """ 
    SINTAXIS DE GETTERS
    @property
    def attribute(self):
        return self._attribute

    SINTAXIS DE SETTERS
    @attribute.setter
    def attribute(self, attribute):
        self._attribute = attribute
    """


# EJEMPLOS DE USO
    
google = Invoice("Google", 100)

print(google.formatter())
# Google owes: $100

# Obtener los valores de los atributos protegidos gracias a @property
print(google.client)            # Google
print(google.total)             # 100

# Modificar los valores gracias al SETTER
google.client = "Yahoo"         # Se modifica el valor
print(google.client)            # Yahoo

"""
El atributo 'total' no tiene SETTER, por lo que si intentamos ejecutar este
código, obtendríamos un error:
"""

# google.total = 200            # AttributeError: can't set attribute 'total'