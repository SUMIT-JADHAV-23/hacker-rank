# """
# given a number n ,for each interger i in the renge from 1 ti n print value per line
# if i is multiple of 3 and 5 print"fizzBuzz"
# if i is multiple of 3 and not 5 print"fizz"
# if i is multiple of 5 and not 3 print"Buzz"
# if i is not multiple of 3 and 5 print (number i)
# """
# # in first attmept code done....

# def fizzBuzz(n):
#     # Write your code here
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             print("FizzBuzz")
#         elif i%3==0 and i%5!=0:
#             print("Fizz")
#         elif i%5==0 and i%3!=0:
#             print("Buzz")
#         else:
#             print(i)
                

# if __name__ == '__main__':
    
#     n = int(input().strip())

#     fizzBuzz(n)
"""
python- shape class with area method

implement of two case rectangle and Circle
Rectangle-the constructur for Rectangle must take two arrguments that denote L,W of Rectangle
         class must have area method that returns area of Rectangle
Circle-the constructor must take 1 argument as radius of Circle
      the Circle class must have area that of Circle. to Implement area use math.pi constant

Your implementation of all class will be tested by provided code stub on several input files 
each input file contain  serveral qureis and each query constructan object of one of the classes and .
print the area of object to the standard output with exactly 2 decimal points
 
input -in the 1 line , there is single int , q , the number of queries 
then q lines follow . in the i of them ,there are space seprated  parameters
the Firstof them denotes the shape of constructor and the remainng parameter denote the parameter for constructor

sample input= query no. of querys 2,query parameter["circle 1" "reactangle 2 3 "] 


"""
import math
import os
import random
import re
import sys

# class Rectangle:

#     pass
# class Circle:
#     pass

# if __name__== '__main__':
#     q=int(input())
#     queries=[]
#     for _ in range(q):
#         args=input().split()
#         shape_name,params=args[0],tuple(map(int,args[1:]))
#         if shape_name=="rectangle":
#             a,b =params[0],params[1]
#             shape =Rectangle(a,b)
#         elif shape_name=="circle":
#             r=params[0]
#             shape=Circle[0]
#         else:
#             raise ValueError("invalid shape type")
#         fqtr.write("%.2f\n"%shape.area())
#     fqtr.close()
                                        

# here is the given code we need to only def area of rect and circle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2

# if __name__ == '__main__':
#     fqtr = open('output.txt', 'a')  # Use a specific file name or adjust for your platform
#     q = int(input())
#     for _ in range(q):
#         args = input().split()
#         shape_name, params = args[0], tuple(map(int, args[1:]))
#         if shape_name == "rectangle":
#             a, b = params[0], params[1]
#             shape = Rectangle(a, b)
#         elif shape_name == "circle":
#             r = params[0]
#             shape = Circle(r)
#         else:
#             raise ValueError("invalid shape type")
#         fqtr.write("%.2f\n" % shape.area())
#     fqtr.close()


"""
#The self parameter is a reference to the instance of the class.
#It is a convention in Python to use self as the first parameter of instance methods.
#self allows you to refer to the instance's attributes within the method.
#Inside the __init__ method, you initialize the attributes of the object (length and width) 
#with the values passed as arguments during the object creation.
#when you create an instance of the Rectangle class like this: rectangle_instance = Rectangle(10, 5), 
#the __init__ method is automatically called with length=10 and width=5
"""

"""
#It takes three parameters: self, length, and width.
#self is a reference to the instance of the class.
#length and width are the dimensions of the rectangle, which are used to initialize the attributes of the object

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.width * self.length

# # Creating an instance of the Rectangle class
# area = Rectangle(length=5, width=10)

# # Accessing attributes and calling the area method
# print(area.length)  # Output: 5
# print(area.width)   # Output: 10
# print(area.area())  # Output: 50
"""

"""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

# Creating an instance of the Circle class with radius 5
circle_instance = Circle(5)

# Accessing the radius attribute
print("Radius:", circle_instance.radius)  # Output: 5

# Calculating and printing the area of the circle
print("Area:", circle_instance.area())    # Output: 78.54 (approximate)

"""

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.width*self.length
        pass

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*radius**2
        pass


q=int(input())
for _ in range(q):
    args = input().split()
    shape_name, params = args[0], tuple(map(int, args[1:]))
    print("Shape:", shape_name)
    print("Params:", params)
    if shape_name == "rectangle":
        a, b = params[0], params[1]
        shape = Rectangle(a, b)
    elif shape_name == "circle":
        radius = params[0]
        shape = Circle(radius)
    else:
        raise ValueError("invalid shape type")
    area = shape.area()
    print (area)
    # print("Area:", area)
    print("{:.2f}".format(area))




