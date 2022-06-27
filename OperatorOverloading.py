"""
Any method that start and end with under score '__' is called dunder method for example __init__.
It is a special type of method.
__init__ is a special type of constructor.
__add__ is a dunder method use to overload operators.
"""

class Employee:
    no_of_workingHours = 9
    def __init__(self, aname, asalary):
        self.name = aname
        self.salary = asalary
        print(f"My name is {self.name} and my salary is {self.salary}")
    def printFunc(self):
        return f"Name of Employee is {self.name}. Salary of Employee is {self.salary}. Working hours of Employee is {self.no_of_workingHours}"
    @classmethod #This is class method
    def change_hours(cls, newhours):
        cls.no_of_workingHours = newhours
    @classmethod
    def from_Str(cls, new_string):
        # params = new_string.split("-")
        # return cls(params[0], params[1])
        return cls(*new_string.split("-"))
    @staticmethod
    def print_anything(string):
        return (f"Parameter is \'{string}\'")
    def __add__(self, other): #operator overloading
        return self.salary + other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self): #It is also a special type of function use to represent attributes of object in a string.
        return f"(\"{self.name}\", {self.salary})"
    def __str__(self):
        return self.printFunc()

emp1 = Employee("Subhan", 75757)
emp2 = Employee("Hassaan", 757570)
print("emp1 + emp2 will add the salary of both employees which is : ", emp1 + emp2)
print("emp1 / emp2 will divide the salary of both employees and will give us the answer and which is : ", emp1 / emp2)
print(emp1.__repr__())

