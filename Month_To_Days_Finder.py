#Input of the month by the user.
month = input("Please enter the name of the month: ")

#Finding the days for each month the user wants.

if month == "April" or month == "June" or month == "September" or month == "November":
    days = 30
elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    days = 31
else:
    month == "February"
    days = "28 or 29"
print(month, "has", days,"days in it")
    
