import time

import datetime

initial = time.time()
print(initial)
for i in range(45):
    print("This is for loop.")
print("This is a time taken to run For loop ", time.time() - initial)
initial2 = time.time()
print("This is second initial", initial2)
k = 0
while k < 45:
    print("This is while loop.")
    k += 1
print("This is a time taken to run While loop", time.time() - initial2)

localTime = time.asctime(time.localtime(time.time()))
print(localTime)
time.sleep(2)
print(datetime.datetime.now())
