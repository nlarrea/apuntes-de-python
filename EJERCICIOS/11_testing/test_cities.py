import unittest

from funciones import get_formated_str

class CitiesTestCase(unittest.TestCase):
    """ tests for funciones.py """

    def test_city_country(self):
        """ Do entries like 'Santiago, Chile' work? """
        formatted_str = get_formated_str("santiago", "chile")
        self.assertEqual(formatted_str, "Santiago, Chile")
    
    def test_city_country_population(self):
        """ Do entries like 'santiago, chile, 50000' work? """
        formatted_str = get_formated_str("santiago", "chile", 50000)
        self.assertEqual(formatted_str, "Santiago, Chile - population 50000")


if __name__ == "__main__":
    unittest.main()