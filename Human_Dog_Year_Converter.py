#Human to Dog (years) converter#

#Input of the human age.
human_years = int(input("Please Enter your age: "))

#Conversion of the years to dog's years.

if human_years < 0:
    print("Please enter a non-negative number")
elif human_years <= 2:
    dog_age = human_years * 10.5
else:
    dog_age = 21 + (human_years - 2) * 4
print("You are", human_years, "in human years")
print("You are", dog_age, "in dog years")
