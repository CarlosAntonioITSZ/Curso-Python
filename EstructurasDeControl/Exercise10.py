
'''
Write a program that says whether a keypad
number is a cousin or not.
'''
import math


number=int(input("Enter a number: "))


for i in range (2,number):
    cousin=True
    #---------------------------------
    for j in range(2,i):
        if i%j==0:
            cousin=False
            break
    #---------------------------------
    if cousin==True:
        print(i,end=" ")
    
