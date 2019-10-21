#Input of the year by the user.

year =int(input("Enter current year: "))

#Find if the year is a leap_year or not.

if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

#Output of the finding.

if leap_year == True:
    print( year, "Is a leap year! ")
else:
    print( year, "Is not a leap year! ")
