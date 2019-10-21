#Functions of the program.
def cube(number):
    return (number ** 3)
def by_threeshould():
    return cube
def by_three():
    if number % 3:
        return by_threeshould and print(cube(number))
        
#Input of the number by the user.
number = int(input("Enter your preferred number here: "))       
print(by_three())

