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

obj1 = Employee("Subhan", "Zaheer")
obj2 = Employee("Ahmad", "Iqbal")
print(obj2.email)
obj2.emailset = "this.that@subhan.code"
print(obj2.fname)
del obj2.emaildel
print(obj2.email)

# def myFunc(func):
#     return func()
# @myFunc
# def mine():
#     print("My name is Subhan Zaheer.")
#
# # mine = myFunc(mine)
# print(mine)