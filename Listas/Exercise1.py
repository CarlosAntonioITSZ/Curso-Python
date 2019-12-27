#Exercise1

'''
Carry out a program that initializes a 
list with 10 random values ​​(from 1 to 10)
and then shows on the screen each element 
of the list along with its square and its cube.
'''
#@CarlosAntonio

import random

myList=[]

for i in range (0,10):
    myList.append(random.randrange(1,10))
    print("Number: ",myList[i], "Square: ", myList[i]**2,"Cubed: ",myList[i]**3)

print("")
print(myList)