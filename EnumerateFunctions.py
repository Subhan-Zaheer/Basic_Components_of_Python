ls = ["Rice", "Roti", "Daal", "Chicken"]
i = 0
"""
It is a conventional way to do the things.
"""
print("This is the conventional way to do things.")
for item in ls:
    if i % 2 == 0:
        print(f"We will buy {item}")
    i += 1

"""
Now we will use enumerate function to solve our problem and make life easy.
"""

print("\nNow we are doing same thing using enumerate function.")
for index, item in enumerate(ls):
    if index % 2 != 0:
        print(f"We will buy {item}")