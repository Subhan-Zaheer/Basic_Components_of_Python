# l = 10
# def func1(n):
#     #l = 5
#     m = 8
#     global l
#     l= l + 45
#     print(n)
#     print(l, m)
#
# func1("This is func1")
# print("This outside func1")
# print(l)

c = 15
def anotherFunc():
    c = 30
    def nestedFunc():
        global c
        c = 12
        print("Before printing nested function", c)
        print("After calling nested function", c)



anotherFunc()