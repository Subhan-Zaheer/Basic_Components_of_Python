def printstr1(string):
    return f"This function \'{string}\' as an argument."

def addWrong(a, b):
    return f" The sum is {a + b + 1} which is wrong..... I know!"


print("The name of function is ", __name__)
if __name__ == '__main__':
    """
    If we import this file to another pycharm file than this code 
    under main function will not be executed.
    """
    print(printstr1("My name is Subhan."))
    print(addWrong(5, 6))