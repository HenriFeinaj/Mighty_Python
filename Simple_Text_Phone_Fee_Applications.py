#Input of air minutes and text messages used.

minutes_plan = 50
text_plan = 50
monthly_charge = 15.00

#Input of extra minutes and texts used by the user.

extra_time = int(input("Enter the surpassed minutes used : "))
extra_texts = int(input("Enter the surpassed texts used : "))

#Calculation of further charge.

minute_charge = monthly_charge + extra_time * 0.25
text_charge = monthly_charge + extra_texts * 0.15

#Calculation of final payment and calculation after applying taxes.

charge_before_support = minute_charge + text_charge + monthly_charge

pre_final_charge = charge_before_support + 0.44
final_charge_1 = pre_final_charge * 0.05
final_charge_2 = final_charge_1 + monthly_charge 

#Final output of the charge.

print("The total amount of your bill this month is: ", final_charge_2, "$")
