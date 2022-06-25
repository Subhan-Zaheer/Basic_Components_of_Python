class A:
    classvar1 = "I am a class variable in class A."
    def __init__(self, var):
        self.var1 = "I am a var 1 in class A."
        self.classvar1 = "Instance variable in class A constructor."
        self.special = "Special Variable"
        print(f"Variable is {var}")

class B(A):
    classvar2 = "I am a class variable in class B."
    def __init__(self):
        self.var1 = "I am a var 1 in class B."
        super().__init__("Var B")
        self.classvar1 = "Instance variable in class B constructor."

a = A("Var")
b = B()
print(b.special)
print(b.var1, b.classvar1)