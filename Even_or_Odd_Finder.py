#EVEN/ODD FINDER
#Input of an interger by the user.

number = int(input("Enter only an integer: "))

#Find if the number is even or odd.

if number % 2 == 1:
    print(number, " ===> odd")
else:
    print(number, " ===> even")
