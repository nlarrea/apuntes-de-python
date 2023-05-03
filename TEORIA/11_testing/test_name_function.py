import unittest         # necesario para realizar los tests

# importamos la función que queremos utilizar
from testear_funciones import get_formated_name

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

if __name__ == "__main__":
    unittest.main()