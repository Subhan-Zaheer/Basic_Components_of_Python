class Employee:
    no_of_workingHours = 9
    def __init__(self, aname, asalary):
        self.name = aname
        self.salary = asalary
        print(f"My name is {self.name} and my salary is {self.salary}")
    #
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

subhan = Employee("Subhan", 100000)
ahmad = Employee("Ahmad", 100000)
# subhan.name = "Subhan Zaheer"
# subhan.sal = 10000
# ahmad.name = "Ahmad Iqbal"
# ahmad.sal = 10000
# print(subhan.__dict__)
# print(Employee.__dict__)
# print(ahmad.__dict__)
# print(subhan.printFunc())
# print(subhan.no_of_workingHours)
# Employee.no_of_workingHours = 11
# print(Employee.no_of_workingHours)
# print(subhan.no_of_workingHours)
# subhan.change_hours(7)
# print(subhan.no_of_workingHours)
Hassaan = Employee.from_Str("Hassaan Ahmad-90000")
# print(Hassaan.name)
print(Hassaan.print_anything("This is Argument"))
print(Employee.print_anything("From Employee Instance"))
