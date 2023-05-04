print("01 - EMPLEADO\n")
"""
Crea una clase llamada 'Employee'. El método '__init()' debe recibir un nombre,
un apellido y un salario anual, y guardar cada dato como atributos. Crea un
método llamadao 'give_raise()' que añada 5000€ al salario anual por defecto,
pero que también acepte diferentes valores.
Crea un test para la clase. Escribe dos métodos de testing: 'test_give_default_
raise()' y 'test_give_custom_raise()'. Usa el método 'setUp()' para no tener
que crear instancias de la clase constantemente y asegúrate de que ambos tests
pasan.
"""

class Employee:
    def __init__(self, first, last, anual_salary):
        self.first_name = first
        self.last_name = last
        self.anual_salary = anual_salary
    
    def give_raise(self, salary_raise=5000):
        self.anual_salary += salary_raise


# tests result:
#
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK