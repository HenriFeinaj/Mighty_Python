#Function body.

def factorial(n):
    if n==0:
        return 1
    elif n < 0:
        return "The number you have entered should be a positive integer!"
        break
    else:
        return n * (factorial(n-1))
    
#Main build

x = int(input("Please enter only a positive integer: "))
factorial(x)


