#Messages given to the user with main goal to understand the flow of the program.
print("Input some integers to calculate their sum and average.")
print("Input of the number 0 terminates the program!")

#Variables of the program.
count = 0
sum = 0
number = 1

#Calculations alongside with the print of the output.
while number >= 1:
	number = int(input(""))
	sum = sum + number
	count += 1

if count == 0:
	print("You can't use 0 so give numbers another try :D ")
else:
	print("The average of the numbers is: ", sum / (count-1))
	print("And the Sum of the previous numbers is: ", sum)
