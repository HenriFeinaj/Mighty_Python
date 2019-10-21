#Simple Calculator 1.0

# Adding function.
def add(x, y):
   return (x + y)

# Substraction function.
def subtract(x, y):
   return (x - y)

# Multiplication function.
def multiply(x, y):
   return (x * y)

# Division function
def divide(x, y):
   return (x / y)

#Operation of the program selected by the user.

print("Now you need to select from 4 choices the operation you desire the program to run")
print("1st choice ===> Adds the 2 numbers! ")
print("2nd choice ===> Substracts the 2 numbers! ")
print("3rd choice ===> Multiplies the 2 numbers! ")
print("4th choice ===> Divides the 2 numbers! ")

# Input of the user.

choice = int(input("Enter the number of the operation: "))

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if choice == 1:
   print(num_1,"+",num_2,"=", add(num_1,num_2))

elif choice == 2:
   print(num_1,"-",num_2,"=", subtract(num_1,num_2))

elif choice == 3:
   print(num_1,"*",num_2,"=", multiply(num_1,num_2))

elif choice == 4:
   print(num_1,"/",num_2,"=", divide(num_1,num_2))
else:
   print("Invalid input")
