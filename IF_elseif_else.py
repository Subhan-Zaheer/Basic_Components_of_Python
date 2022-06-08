print("Enter Num1 : ")
num1 = int(input())
print("Enter Num2 : ")
num2 = int(input())
operator = input("Enter one operator from the following : \n+\n-\n*\n/\n")
if operator != '+' and operator != '-' and operator != '*' and operator != '/':
    print("Invalid Operator.")
else:
    if operator == '+':
        if (num2 == 9 and num1 == 56) or (num2 == 56 and num1 == 9):
            print("Sum of two numbers is 77")
        else:
            print("Sum of two numbers is : ", num1+num2)
    elif operator == '-':
        print("Subtraction of two numbers is : ", num1-num2)
    elif operator == '*':
        if (num2 == 45 and num1 == 3) or (num2 == 3  and num1 == 45):
            print("555")
        else:
            print("Multiplication of two numbers is : ", num1*num2)
    else:
        if (num2 == 6 or num1 == 56) and (num1 != 0):
            print("4")
        else:
            print("Division of two numbers is :", num1/num2)