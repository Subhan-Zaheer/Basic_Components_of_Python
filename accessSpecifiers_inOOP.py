"""
Public - Accessible to every one.
Protected - Accessible to specific people.
Private - Only Accessible to you.
"""

class Employee:
    no_of_workingHours = 9 # The way to declare public variable.
    _City = "Lahore" # The way to declare protected variable.
    __address = "Walton Road Lahore" # The way to declare private variable.
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

emp = Employee("Subhan", 7878787)
print(emp._City) # Way to access protected data members of class.
print(emp._Employee__address) # Way to access private data members of class.