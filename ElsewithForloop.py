"""
Else comes with for loop when for loop ends.
for example when for loop reaches to its terminating condition.

"""

sports = ["Cricket", "Football", "Tennis", "Cards"]
for items in sports:
    if items == "Football":
        print("Item found in list")
        break
else:
    print("Item didn't found.")