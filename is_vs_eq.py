"""
== - Value equality - If two Objects have same value.
is - Reference Equality - If two objects refer to same reference.
"""

a = [7, 4, 3]
b = a
if a == b:
    print(f" a == b is : {True}")
if a is b:
    print(f"a is b : {True}")
print(a)
print(b)
b[0] = 0
print(f"After changing the value of list by b we will check our a : {a}")
c = a[:]
if a == c:
    print(f" a == c is : {True}")
if a is c:
    print(f"a is c : {True}")

c[0] = 7
print(f"After changing the value of list by c we will check our a : {a}")
print(f"And our c is {c}")

i = [1, 2, 3]
j = [1, 2, 3]
print(i is j )