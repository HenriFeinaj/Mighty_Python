import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
 
r = int(input("Enter radius of circle: "))
obj = circle(r)


class Cylinder:
  def __init__(self,radius,height):
    self.radius = radius
    self.height = height
  def __str__(self):
    return "Radius: "+ str(self.radius) + ", Height: " + str(self.height)
 
  def getRadius(self):
    return self.radius
  def getHeight(self):
    return self.height
  def getVolume(self):
      return self.radius*self.radius*3.14*self.height
 
#Creating a cylinder object from the Cylinder class
cd = Cylinder(5,10)
 
print(cd)# This will call the function __str__
print("It's volume is "+str(cd.getVolume()))
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))
