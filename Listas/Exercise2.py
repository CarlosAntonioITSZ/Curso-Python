#Exercise2

'''
Create a list and initialize it with 5 character 
strings read by keyboard. Copy the items from the 
list into another list but in reverse order, 
and display their items on the screen.
'''

#@CarlosAntonio

list1=[]

for i in range (0,5):
    list1.append(input("Enter a character: "))


list2=[]
list2.extend(list1)
list2.reverse()

print("")
print("List 1: ",list1)
print("List 2: ",list2)