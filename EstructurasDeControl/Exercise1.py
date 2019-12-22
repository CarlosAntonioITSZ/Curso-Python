#Exercise1
'''
Write a program that reads a number 
and indicates whether it is odd or even.
'''
#@CarlosAntonio

number=int(input("Enter the number"))

if number%2==0:
    print("The number is even")
elif number==0:
    print("Then number us zero")
else:
    print("The number is odd")

