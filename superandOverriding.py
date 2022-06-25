class A:
    classvar1 = "I am a class variable in class A." # Class Variable
    def __init__(self, var):
        self.var1 = "I am a var 1 in class A." # Instance variable.
        self.classvar1 = "Instance variable in class A constructor."
        self.special = "Special Variable"
        print(f"Variable is {var}")

class B(A):
    classvar2 = "I am a class variable in class B." # Class Variable
    def __init__(self):
        self.var1 = "I am a var 1 in class B." #Instance variable.
        super().__init__("Var B") # Parent class constructor with parameter.
        self.classvar1 = "Instance variable in class B constructor."

a = A("Var")
b = B()
print(b.special)
print(b.var1, b.classvar1)