# Input taken from the user.
number = int(input("Enter any number: "))

# Finding whether the number is a prime one or not.
if number > 1:
    for i in range(1, number):
        if (number % i) == 0:
            print("Number: ", number, "is not a prime number")
            break
    else:
        print("Number: ", number, "is a prime number")

#This part is inside the program because the user can enter/
    #Values of 1 or 0 or even negative ones.

else:
    print("Number: ", number, "is not a prime number")
