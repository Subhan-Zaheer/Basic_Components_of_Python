"""
Polymorphism - It means many forms i.e a method can show behaviour in many forms.
In this example mySelf is a function in all classes and have different
behaviour in every class.
So it is an example of Polymorphism.

Important Concepts in OOP: Abstraction, Encapsulation, Inheritance, Polymorphsim, Overriding ..... 
"""

class ElectronicDevice:
    brand = "Orient"
    productId = 123
    weight = 78
    def mySelf(self):
        return f"Hello! I am an Electronic Device. My brand name is {self.brand}. My product id is {self.productId}." \
               f"As I am very heavy weight. So my weight is {self.weight}"

class PocketGadget(ElectronicDevice):
    brand = "Apple"
    productId = 456
    size = 12
    def mySelf(self):
        return f"Hello! I am a Pocket Gadget. My brand name is {self.brand}. My product id is {self.productId}." \
               f"My size is {self.size}. My parent class is Electronic Device."

class Phone(PocketGadget):
    brand = "Samsung"
    productId = 789
    screensize = 15
    def mySelf(self):
        return f"Hello! I am a Phone. My brand name is {self.brand}. My Product Id is {self.productId}." \
               f"My Screen size is {self.screensize}. My Parent class is Pocket Gadget"


machine = ElectronicDevice()
tab = PocketGadget()
a12 = Phone()
print(a12.mySelf())