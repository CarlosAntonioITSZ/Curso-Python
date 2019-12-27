#Exercise2

'''
Write a program that reads a string and 
returns a dictionary with the number of 
occurrences of each character in the string
'''

#@CarlosAntonio

string=input("Enter a string: ")

dicc={}

for i in string:
    dicc[i]=0

print(dicc)