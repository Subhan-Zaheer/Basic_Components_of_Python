class Employee:
    no_of_workingHours = 9
    def printFunc(self):
        return f"Name of Employee is {self.name}. Salary of Employee is {self.sal}. Working hours of Employee is {self.no_of_workingHours}"

subhan = Employee()
ahmad = Employee()
subhan.name = "Subhan Zaheer"
subhan.sal = 10000
ahmad.name = "Ahmad Iqbal"
ahmad.sal = 10000
# print(subhan.__dict__)
# print(Employee.__dict__)
# print(ahmad.__dict__)
print(subhan.printFunc())