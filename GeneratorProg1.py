"""
Iterable - __iter__() or __getitem__()
Itrator -  __next__()
Itration - The process of iterate.
If the object is iterable than it will run __iter__ function
and will create an iterator and then iterator will run
__next__() function to go to next element.
In this way iteration can be done.
"""

def gen(n):

    for i in n:
        yield i



g = gen("Subhan")
print(g)
for i in g:
    print(i)
h = "hassaan"
iter1 = iter(h)
print(iter1.__next__())
print(iter1.__next__())
print(iter1.__next__())
print(iter1.__repr__())
