#Exercise4

''''
Create an application that asks
for a number and calculate its factorial
'''

#@CarlosAntonio

num=int(input("Enter a number: "))
factorial=1

for i in range (1,num+1):
    factorial*=i   

print(factorial)
