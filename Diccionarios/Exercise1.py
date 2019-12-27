#Exercise1

'''
Write a python program that asks for a number 
by keyboard and that creates a dictionary whose
keys are from the number 1 to the indicated number, 
and the values ​​are the squares of the keys.
'''

#@CarlosAntonio

number=int(input("Enter a number: "))
dicc={}

for i in range (1,(number+1)):
    dicc[i]=i**2

print(dicc)