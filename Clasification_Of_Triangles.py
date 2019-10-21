#Program for the classification of triangle.
print("You can enter below the 3 sides of the triange to classify its type. ")

#Input of the side lengths by the user.

sd_1 = int(input("Enter the length of the first side: "))
sd_2 = int(input("Enter the length of the second side: "))
sd_3 = int(input("Enter the lenght of the third side: "))

#Classify the type of the triangle based of the lenghts given above.

if sd_1 == sd_2 or sd_2 == sd_3 or sd_1 == sd_3:
    triangle_type = "Isoceles"
elif sd_1 == sd_2 and side_2 == sd_2 == sd_3:
    triangle_type = "Equilateral"
else:
    triangle_type = "Scalene"

#Print of the output at the user.

print("Type of triangle: ", triangle_type)
