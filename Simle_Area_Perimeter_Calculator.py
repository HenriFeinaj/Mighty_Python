def square_area(side):
    return side ** 2
def square_perimeter(side):
    return side * 4
side = int(input("Enter the side of the square: "))
area = square_area(side)
perimeter = square_perimeter(side)
print("The area of the square is: ", area)
print("The perimeter of the square is: ", perimeter)
