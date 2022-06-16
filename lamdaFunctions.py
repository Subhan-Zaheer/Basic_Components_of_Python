# One liner Functions
# Lambda Functions
def add(a, b):
    return a + b

"""
Syntax of lambda functions
func_name = lambda keyword (args): body of function
"""
minus = lambda a, b: a - b
def a_first(a):
    return a[0]

print(minus(5, 3))

a = [[8, 14], [15, 6], [10, 5]]
a.sort(key = a_first)
print(a)