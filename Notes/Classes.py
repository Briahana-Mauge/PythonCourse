# We use classes to define new types like:
# Basic types: Numbers, Strings, Booleans
# Complex types: Lists, Dictionaries

# When defining a class, we use CapitalLetters to start every word (CamelCase) it unlike snake_case when naming functions
# when creating new methods on the class. 'self' is
# Example: create a new type called 'Point'


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# Now that the new type is defined, we can create objects
# The object is an instance of the class

point1 = Point() # a new point object
point1.x = 10 # makeing an 'x' attribute
point1.y = 20 # makeing an 'y' attribute
point1.draw()

point2=Point() # a new point object that has nothing to do with the 1st one
# print(point2.x) # will return an error because it doesn't have an attribute x like the other point does


# CONSTRUCTOR
# if we want to make a class be more blueprint like so we can avoid situations where one obj has attributes while another instance doesn't,
# we include a constructor function in the class
# the method that gets created at initialization of the class falls under "__init__"
class Pointer:
    def __init__(self,x,y): # self is the obj itself, x & y are the arguments passed that we want as attributes
        self.x = x
        self.y=y
   
    def move(self):
        print("move")

    def draw(self):
        print("draw")
pointer = Pointer(10,20)
print(pointer.x)

# Problem: define a new type called person with a name attribute and talk method

class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi, I am {self.name}")

name = input("What is your name? ")
bri = Person(name)
bri.talk()

# INHERITENCE
 # mechanism for reusing code

# Problem : both the dog and cat class has a walk method. istead of repeating ourselves twice, can we make that method reusable for both classes?
"""
class Dog:
    def walk(self)
        print("walk")

class Cat:
    def walk(self)
        print("walk")
"""

# create a universal class called Mammal that holds all shared methods between dogs and cats

class Mammal:
    def walk(self):
        print("walk")
 
class Dog(Mammal): # will inherit all methods from the mammal class
    def bark(self):
        print("woof")

class Cat(Mammal): # will inherit all methods from the mammal class
    pass #if you dont have a uniqie method for the class, use 'pass' so that it's not empty

dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
# cat1.bark() #Will not work because only the dog has this method - AttributeError: 'Cat' object has no attribute 'bark'