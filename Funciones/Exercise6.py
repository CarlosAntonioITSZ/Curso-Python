'''
Create a recursive function that allows you
to calculate the factorial of a number. 
Make a main program where an integer 
is read and the factorial result is displayed.
'''

def getFactorial(num):
    if num == 0 or num ==1:
        return 1
    if num<0 or num >100:
        raise TypeError ("Those values ​​are not allowed")
    else:
        return num*getFactorial(num-1)

try:
    num=int(input("Enter a num: "))
    print(getFactorial(num))
except ValueError:
    print("It´s not a number")