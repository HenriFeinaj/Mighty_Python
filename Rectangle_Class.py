#Rectangle class with attributes pritnting area, width and length.
#Note: Area of Rectangle = width * length

class rectangle:
    def __init__ (self, width, length):
        self.width = width
        self.length = length
    def print_area(self):
        print ("The area of this rectangle is ", float(self.width * self.length), "cm.")
        print ("The width is", self.width, "cm while the length is", self.length, "cm.")

rec1 = rectangle (8,4)
rec1.print_area()
