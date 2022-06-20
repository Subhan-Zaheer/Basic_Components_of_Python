
"""-------------------Map Function---------------------------------"""

numbers = ["3", "34", "35"]
"""If I want to convert elements of numbers to int
    then the conventional way to do this is using for loop."""
print(type(numbers[0]))
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])



"""Another way to do this is to use map function.
    Map function is used if you want to apply same function
    on each element of iterable.
"""
a = tuple(map(int, numbers))

print(type(a[0]))
sq = lambda x: x*x
newlist = [2, 3, 6, 5, 4, 7, 9]
square = list(map(sq, newlist))
print(f"Square of 5 is {sq(5)}")
print(square)


sq = lambda x: x * x
cube = lambda x: x * x * x
ls = [sq, cube]
for i in range(5):
    newls = list(map(lambda x: x(i), ls))
    print(newls)


"""-------------------Filter Function---------------------------------"""
"""Filter Function will filter the value"""
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_greater_than_5(num):
    return num > 5
for item in num:
    print(is_greater_than_5(item))

gr_than_5 = list(filter(is_greater_than_5, num))
print(gr_than_5)

"""-------------------Reduce Function---------------------------------"""
import functools
ls = [1, 2, 3, 4]
"""if we want to add the value of ls than we will do..."""
num = 0
for i in ls:
    num = num + i

print(num)

"""If we want to do the same thing in one line than we will use reduce function"""
newNum = functools.reduce(lambda x, y: x * y, ls)
print(newNum)