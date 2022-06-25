"""
Diamond Shape Problem is an ambiguity. It happens when we are doing
multiple inheritance. Grand child class face a confusion if there is a function
or an attribute which is present in its all parent class or the root class
then the function or an attribute from which class will be used.
Python syntax can solve this problem but this is a problem for other
languages like C++. So we should avoid this other wise your C++ compiler
will get confuse and there will be an error.
"""

class A:
    def thisclass(self):
        print("This function is from class A.")

class B(A):
    def thisclass(self):
        print("This function is from class B.")

class C(A):
    def thisclass(self):
        print("This function is from class C.")

class D(C, B):
    def thisclass(self):
        print("This function is from class D.")
    pass


a = A()
b = B()
c = C()
d = D()
d.thisclass()