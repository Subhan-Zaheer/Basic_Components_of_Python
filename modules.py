import random
"""
This module helps to generate random number.
"""
random_number = random.randint(0, 8)
print(random_number)

rand = random.random() * 100
print(rand)
ls = ["Subhan", "Hassaan", "Ahmad", "Hamza"]
choice = random.choice(ls)
print (choice)

import operator
"""
This module have basic functions performed on operators.
"""
print(operator.add(5, 6))

num1 = int(input("Enter a number1 : "))
num2 = int(input("Enter a number2 : "))
if operator.eq(num1, num2):
    print("Both numbers are equal.")
else:
    print("Numbers are not equal.")