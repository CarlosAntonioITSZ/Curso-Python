#Exercise1
'''
Create a “calculate MaxMin” function that receives
 a list with numerical values ​​and returns 
 the maximum and minimum value. 
 
 Create a program that asks for numbers 
 by keyboard and displays the maximum and minimum, 
 using the previous function.
'''
#@CarlosAntonio

list=[]

for i in range(0,10):
    while True:
        try:
            element=int(input(f"Enter a number {i}: "))
            list.append(element)
            break
        except:
            print("Enter a number")
        

def calculateMaxMin(list):
    list.sort()
    print("Minimum: ",list[0])
    print("Maximum: ",list[len(list)-1])

calculateMaxMin(list)