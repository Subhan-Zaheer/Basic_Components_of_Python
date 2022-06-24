
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

class Player:
    no_of_game = 4
    def __init__(self, aname, agame):
        self.name = aname
        self.game = agame
    def print_func(self):
        return f"Name of Player is {self.name}. Game of Player is {self.game}."

# Here keep in view that pycharm will call constructor of first class
# in sequence in case of Multiple Inheritance.
# If there is a method or an Attribute which is present in both classes
# then it will choose one of first class in sequence of Inheritance.
class CoolProgrammer(Employee, Player):
    languages = "C++"
    def printLang(self):
        print(f"Language is {self.languages}")

# print("Objects from Employee class")
subhan = Employee("Subhan", 100000)
ahmad = Employee("Ahmad", 100000)
dawood = Player("Dawood", ["Cricket", "Cards"])
print(dawood.print_func())
Hamza = CoolProgrammer("Hamza", "1949")
# print("Objects from Programmer class")
# Hamza = Programmer.from_Str("Hamza Shah-90909")
# Dawood = Programmer.from_Str("Dawood-10000")
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
# Hassaan = Employee.from_Str("Hassaan Ahmad-90000")
# # print(Hassaan.name)
# print(Hassaan.print_anything("This is Argument"))
# print(Employee.print_anything("From Employee Instance"))
