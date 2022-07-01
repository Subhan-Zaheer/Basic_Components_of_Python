"""
Object Introspection is basically to know about that object i.e Its class type and many more.
Object Introspection can be done by following ways:
1. Type function
2. Id function
3. Dir function
4.
"""

import inspect
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printDetails(self):
        return f"First Name of Employee is {self.fname} and Last Name of Employee is {self.lname}"
    @property
    def email(self):
        # if self.fname == None or self.lname == None:
        #     return "Email is not set. Please set it using setter function."
        return f"{self.lname}.{self.fname}@subhan.code"
    @email.setter
    def emailset(self, string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]
    @email.deleter
    def emaildel(self):
        self.fname = None
        self.lname = None

emp1 = Employee("Subhan", "Zaheer")
print(emp1.__sizeof__())
print(type(emp1))
print(id(emp1))
print(dir(emp1))
print(inspect.getmembers(emp1))