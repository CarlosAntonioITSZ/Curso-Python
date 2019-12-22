#Exercise 3

'''
Given the legs of a right triangle, 
calculate its hypotenuse.
'''

#@CarlosAntonio

import math

a=float(input("Enter the leg A: "))
b=float(input("Enter the leg B: "))

h=math.sqrt((a**2)+(b**2)) #Formula to have the hypotenuse

print(f"The hypotenuse is {h:.2f}")
