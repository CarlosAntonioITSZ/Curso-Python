#Exercise9

'''
Perform an algorithm that shows
 the multiplication table of a number 
 entered by keyboard.
'''

#@CarlosAntonio

number=int(input("Enter a number: "))

for i in range(1,11):
    print(number,"*",i,"=",(number*i))