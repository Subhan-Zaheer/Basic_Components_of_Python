def name_Printing(a, b, c, d, e):
    """
    This function is taking arguments but
    it can only accept limited number of arguments.
    There is no flexible way to increase the number of arguments for this function.
    """
    print(a, b, c, d, e)


name_Printing("Ahmad", "Hassaan", "Subhan", "Hamza", "Sheikh")


def name_Printingargs(normal, *args, **kwargs):
    """
    So it is the conventional way to increase the number of arguments
    in our function flexibly.
    Sequence of arguments should be:
        normal args, *args, **kwargs
    """
    print(normal)
    print("The Students in class are : ")
    for item in args:
        print(item)
    print("\nNow we will show the expertise of each student : ")
    for key, val in kwargs.items():
        print(f"{key} is a {val}.")


ls1 = ["Subhan", "Hassaan", "Waleed", "Ahmad"]
dict = {"Subhan" : "Programmer", "Hassaan" : "Web Developer", "Waleed" : "Graphic Designer", "Ahmad" : "Software Engineer"}
normal = "This is a normal argument"
name_Printingargs(normal, *ls1, **dict)