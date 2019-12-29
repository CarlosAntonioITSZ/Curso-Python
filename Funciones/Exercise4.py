#Exercise1
'''
Design a function that calculates the area 
and perimeter of a circle. Use this function 
in a main program that reads the radius of 
a circle and shows its area and perimeter.
'''
#@CarlosAntonio
from math import pi

def calculate(radius):
    print("Area: {:.2f}".format(pi*(radius**2)))
    print("Perimeter: {:.2f}".format(2*pi*radius))

calculate(4)