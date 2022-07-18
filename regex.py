import re
mystr = """Methods are functions that belongs to the class.

There are two ways to define functions that belongs to a class:

Inside class definition
Outside class definition
In the following example, we define a function inside the class, and we name it "myMethod".

Note: You access methods just like you access attributes; by creating an object of the class and using the dot syntax (.):"""

# pattern = re.compile("lass")
# pattern = re.compile(".ol")
# pattern = re.compile("^Methods")
# pattern = re.compile(r"\(.\):$")
# pattern = re.compile(r"ll+o*")
pattern = re.compile(r" {2}")

matches = pattern.finditer(mystr)
for item in matches:
    print(item)