#Exercise7

'''
Make a program that requires a number of minutes 
and display on screen how many hours and minutes.
For example: 1000 minutes is 16 hours and 40 minutes.
'''
#@CarlosAntonio 

minutes=int(input("Enter the minutes: "))
hours=minutes//60
minutes2=minutes%60
print("")

print(f"{minutes} minutes is {hours} hours and {minutes2} minutes")