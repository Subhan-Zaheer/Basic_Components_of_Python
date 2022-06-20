ls = ["Subhan", "Hassaan", "Ahmad"]
print(" This is the conventional way to do things.")
for item in ls:
    """ This is the conventional way to do things."""
    print(item, "and", end=" ")
print("my other friends.")
"""Now using Join function."""
print("\nNow using Join function.")
b = ", ".join(ls)
print(b)
print(b, "my other friends.")

