#==============================================================================================#
#Circle Class printing its area and perimeter using the given attributes.

#Note: Area of Circle = π*r^2, Perimeter of Circle = 2*π*R
#π = 3.14

class circle:
    def __init__(self, radius):
        self.radius = radius
    def print_methods(self):
        print ("The area of this circle is", (float(self.radius)*float(self.radius)* 3.14), ".")
        print ("The perimeter of this circle is", (2 * 3.14 * float(self.radius)), ".")

circ1 = circle (3)
circ1.print_methods()
#===============================================================================================#
