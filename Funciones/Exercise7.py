#Exercise7
'''
Create a function that calculates the MCD of two numbers 
by the Euclid method. Euclid's method is as follows:

The largest number is divided by the smallest.

If the division is exact, the divisor is the MCD.

If the division is not exact, we divide the divisor
among the rest obtained and continue in this way 
until an exact division is obtained, the last divisor being the MCD.

Create a main program that reads two integers and displays the MCD.
'''
#@CarlosAntonio
def maxAndMin(a,b):
    if a>b:
        return a,b
    else: 
        return b,a

def mcd(a,b):
    max,min=maxAndMin(a,b)
    res=max%min

    if max%min==0:
        return min
    else: 
        return mcd(min,res)
    
        
print(mcd(24,16))