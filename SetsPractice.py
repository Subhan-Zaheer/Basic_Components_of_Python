ls = [1, 2, 2, 3, 4]
s1 = set(ls)
s1.add(5)
print(s1)
s1.remove(4)
print(s1)
s1 = (s1.union([4, 5, 6]))
print(s1)