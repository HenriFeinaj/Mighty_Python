#Input of the user.
number = int(input("Enter number:"))
#Calculations of the digits.
count = 0
while( number > 0 ):
    count = count+1
    number = (number // 10)
#Print of the output based on the given input.
print("The number you have entered has:",count, "digits!")
