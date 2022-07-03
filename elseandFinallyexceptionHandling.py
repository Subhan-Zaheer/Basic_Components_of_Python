"""
Finally part always run either program executes try part or exception part.
If Except part will run than else will not run and vice versa.
"""

f = open("Subhan3.txt")
try:
    f1 = open("Subhan2.txt")
except Exception as e:
    print(e)
else:
    print("This will only run when except does not execute.")
finally:
    f.close()