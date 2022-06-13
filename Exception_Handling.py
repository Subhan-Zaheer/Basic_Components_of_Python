num1 = 0
print("Enter number 1 : ")

try:
      num1 = int(input())

except Exception as e:
      print(e)
      print("Ypu must enter a integer number.")
      num1 = int(input())

num2 = 0
print("Enter number 2 : ")

try:
      num2 = int(input())

except Exception as e:
      print(e)

print("The sum of two numbers is :",
      num1 + num2, ", because if you entered a string in integer than we have set the value of that number as 0")
