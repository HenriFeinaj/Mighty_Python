#========================================================================================#
#========================================================================================#

#Creating a class named Dog constructed by a name and age.
#Using the same Dog class, instantiating three new dogs, each with a
#different age. Then writing a function called, get_biggest_number(),that
#takes any number of ages(*args) and returns the oldest one. Then outputs
#the age of the oldest dog like so: The oldest dog is 7 years old.

class Dog:
    def __init__ (self, name, age):
        self.name=name
        self.age=age
    

dog1 = ("Steve", 7)
dog2 = ("Bucky", 6)
dog3 = ("Nat",4)

def get_biggest_number():
    print ("The oldest dog is", max(7,4,6), "years old.")


get_biggest_number()


#========================================================================================#
#========================================================================================#

