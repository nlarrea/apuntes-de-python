import unittest
from clases import Employee

class TestEmployee(unittest.TestCase):
    """ Tests for the class Employee. """
    def setUp(self):
        self.my_employee = Employee("Naia", "Larrea", 38600)
        self.salary_before = self.my_employee.anual_salary

    def test_give_default_raise(self):
        """ Test that default salary raise works properly. """
        # modify the salary (default salary raise = 5000)
        self.my_employee.give_raise()
        # check if it works properly
        self.assertEqual(self.my_employee.anual_salary, self.salary_before+5000)
    
    def test_give_custom_raise(self):
        self.my_employee.give_raise(8000)
        self.assertEqual(self.my_employee.anual_salary, self.salary_before+8000)


if __name__ == '__main__':
    unittest.main()