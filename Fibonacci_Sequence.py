#Fibonacci Program.
#=================================================
#Function.

def fibonacci(n):

  if n == 0:
    return 0

  if n == 1:
    return 1

  else:
    return fibonacci(n-1) + fibonacci(n-2)
#=================================================

#Input of a number.

n = float(input("Enter a number: "))

#=================================================

#Print of the output.

print("Fibonacci output: ", fibonacci(n))

#=================================================
