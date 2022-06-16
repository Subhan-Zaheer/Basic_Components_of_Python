#Iteration vs Recursion
# n! = n * n-1 * n-2 * n-3 ..... 1
# n! = n * (n-1)!

def factorial_Iterative(n):
    """
    Iterative Approach
    :param n: Integer
    :return:  n * n-1 * n-2 * n-3 ..... 1
    """
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def factorial_Recursive(n):
    """
    Recursive Approach
    :param n: Integer
    :return:  n * n-1 * n-2 * n-3 ..... 1
    """
    if n==1 or n == 0 : return 1
    else :
        return n * factorial_Recursive(n-1)


def fabonacci(n):
    """
    :param n: Integer
    :return:  nth number in fabonacci series
    """
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    else: return fabonacci(n-1) + fabonacci(n-2)



number = int(input("Enter a number "))
print("Factorial of ", number, " through iterative approach is : ", factorial_Iterative(number))
print("Factorail of ", number, " through recursive approach is : ", factorial_Recursive(number))
print(number, "th number in Fabonacci is : ", fabonacci(number))