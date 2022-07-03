"""
There are four types of comprehensions:
List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Genrator Comprehensions
"""
# Conventional way to process lists.

# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
# print(ls)

# Now with generators

# ls = [i for i in range(100) if i % 3 == 0]
# print(ls)

# Conventional way to process dictionaries.

# dict1 = {1 : "item1", 2 : "item2"}

#Now with Comprehensions

# dict2 = {i:f"item{i}" for i in range(1, 11)}
# print(dict2)

# Reversing key value pair through comprehensions.

# dict2 = {value:key for key, value in dict2.items() if key%2 == 0 }
# print(dict2)

# Now set comprehensions

# dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
# print(dresses)

#Now generator comprehensions

# odds = (i for i in range(100) if i%2 == 1)
# for items in odds :
#     print(items)

#Exercise

input1 = int(input("Enter how many values you want to insert in list : "))
ls = []
for i in range(input1):
    input2 = int(input("Enter value here : "))
    ls.append(input2)
choice = int(input("Press 1 for list comprehension \nPress 2 for set comprehension\nPress 3 for generator comprehensions."))
if choice == 1:
    list1 = [item for item in ls]
    print(list1)
elif choice == 2:
    set1 = {item for item in ls}
    print(set1)
elif choice == 3:
    gens = (item for item in ls)
    for c in gens:
        print(c)
