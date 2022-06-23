class Employee:
    no_of_workingHours = 9
    pass

subhan = Employee()
ahmad = Employee()
subhan.name = "Subhan Zaheer"
subhan.sal = 10000
ahmad.name = "Ahmad Iqbal"
ahmad.sal = 10000
print(subhan.__dict__)
print(Employee.__dict__)
print(ahmad.__dict__)