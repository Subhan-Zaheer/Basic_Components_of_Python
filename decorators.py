# def name():
#     print("My name is Subhan Zaheer.")
#
# mySelf = name
# del name
# mySelf()
#
# def funcret(num):
#     if num == 0:
#         return print
#     else:
#         return sum
#
# print(funcret(0))

# def executor(func):
#     func("THIS IS EXECUTOR FUNCTION.")
#
#
# executor(print)

def dec1(func1):
    def exec_now():
        print("This is excecuting now function before func1.")
        func1()
        print("After func1 function")
    return exec_now()

def another_func():
    print("This is another function")

another_func = dec1(another_func)

