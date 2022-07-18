# a = input("What is your name : ")
# b = input("How much did you earn : ")
# if int(b) == 0:
#     raise ZeroDivisionError("b is 0 so we are stopping the program.")
# print(f"Hello! {a}")
# print(b)

c = input("Enter your name : ")
try:
    print(a)
except Exception as e:
    if c == "Subhan":
        raise ValueError("This person is not allowed.")
    print(f"Hello! {c}. Variable a is not defined.")