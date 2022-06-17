# concept of fstrings
import math
import time
"""
Un conventional way of formatting string.
"""
me = "Subhan"
a = "This is %s" % me
print(a)

"""
Moderate way of formatting string.
"""
me1 = "Subhan"
me2 = "Zaheer"
a1 = "This is {} {}"
b = a1.format(me1, me2)
print(b)

"""
F-strings
"""
str1 = f"This is {me1} {me2} {math.sin(90)}"
str2 = f"Sum of 4 and 5 is : {4+5}"
print(str1)
print(str2)
print(time.time())