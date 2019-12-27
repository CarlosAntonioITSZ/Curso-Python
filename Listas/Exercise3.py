#Exercise3

'''

Make a program that initializes a list of
numbers with random values ​​(10 values),
and then orders the elements from least to greatest.
'''

#@CarlosAntonio
import random

list=[]

for i in range (1,11):
    list.append(random.randrange(1,50))

list.sort()

print(list)