#Exercise8
'''
Write a program that prints all the even
numbers between two numbers that are 
requested from the user.
'''
#@CarlosAntonio

a=int(input("Enter the number A: "))
b=int(input("Enter the number B: "))

for i in range(a,b):
    if(i%2==0):
        print(i," ",end="")