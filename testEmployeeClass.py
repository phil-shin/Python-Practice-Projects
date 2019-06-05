#! python
# testEmployeeClass.py - tests the functionality of the Employee class

import unittest
from employeeClass import Employee

class employeeClassTest (unittest.TestCase):
    """ Test for Employee class within employeeClass.py"""
    
    def setUp(self):
        self.employee=Employee('Michael', 'Jordan', 10000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 20000)

unittest.main()
