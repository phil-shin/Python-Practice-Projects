#! python
# employeeClass.py - creates Employee class that has first name, last name, and
# salary attributes, as well as a give_raise function that increases the
# employee's salary

class Employee():
    """ class that models an employee;
        has attributes for first name, last name, and salary;
        has function give_raise to increase salary"""
    
    def __init__(self, firstName, lastName, salary):
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary

    def give_raise(self, salaryRaise=5000):
        self.salary+=salaryRaise
        
