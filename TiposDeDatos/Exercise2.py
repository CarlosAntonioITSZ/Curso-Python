#Exercise2

'''
Calculate the perimeter and area of ​​a given rectangle
its base and height
'''

#@CarlosAntonio

height=float(input("Enter the heigth: "))
base=float(input("Enter the base: "))

area=base*height
perimeter=2*(base+height)

print("")
print(f"The area of rectangle is: {area} cm^2")
print(f"The perimeter of rectangule is {perimeter} cm")