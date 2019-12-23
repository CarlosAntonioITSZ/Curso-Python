#Exercise6

'''
Algorithm that asks for numbers until a zero is entered. 
You must print the sum and the average of all the numbers entered.
'''

#@CarlosAntonio

var=True
sum=0
avg=0

while var==True:
    number=int(input("Enter a number: "))
    sum+=number
    avg+=1
    if(number==0):
        var=False
        print("Sum of the numbers: ",sum,"\nAverage of the numbers: ",sum/avg)

