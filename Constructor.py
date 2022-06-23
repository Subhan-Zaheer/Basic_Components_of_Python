class Employee:
    no_of_workingHours = 9
    def __init__(self, aname, asalary):
        self.name = aname
        self.salary = asalary
        print(f"My name is {self.name} and my salary is {self.salary}")

    def printFunc(self):
        return f"Name of Employee is {self.name}. Salary of Employee is {self.salary}. Working hours of Employee is {self.no_of_workingHours}"

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