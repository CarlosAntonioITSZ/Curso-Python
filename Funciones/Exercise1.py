#Exercise1
'''
Create a program that asks the user for two integers 
and say if one of them is a multiple of the other. 

Create an EsMultiplo function that receives both numbers,
 and returns if the first is a multiple of the second.
'''
#@CarlosAntonio

def EsMultiplo(a,b):
    if a%b==0:
        return "Si es multiplo"
    else:
        return "No multiplo"

while True:
    try:
        a=int(input("Enter a number a: "))
        b=int(input("Enter a number b: "))
        print("")
        print(EsMultiplo(a,b))
        break
    except ValueError:
        print("")
        print("Enter a number please")