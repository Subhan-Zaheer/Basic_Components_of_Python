"""
If our function is taking time to execute
and if we need our function repeatedly than
function caching is used. In function caching
we save input and output value of function and next
time when we need to run that function pycharm will automatically
run the saved value of that function and will save our time.
If we are giving same input every time to that function than it will help
by saving our time.
"""

import time
from functools import lru_cache

@lru_cache(maxsize=10)
def some_print(n):
    time.sleep(n)
    #print("Some print function is executing.")
@lru_cache(maxsize=4)
def fabonacci(n):
    if n == 0:
      return 0
    if n == 1 or n == 2:
      return 1
    # if n<=2: return 1
    return (fabonacci(n-1) + fabonacci(n-2))

def recur_fibo(n):
   if n <= 2:
       return 1
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

if __name__ == '__main__':
    # print("Now we are calling some print function.")
    # choice = int(input("Enter how many value you want to cache."))
    # some_print(3)
    # print("Done... but calling again.")
    # some_print(4)
    # print("Again Done...")
    # some_print(3)
    # print("Again Done...")
    # some_print(4)
    # print("Again Done...")
    for i in range(1, 40):
        fib = fabonacci(i)
        print(f"Fabonacci number of {i}th term is ", fib)


