#Exercise6

'''
Create a program that adds numbers to a
list until we enter a negative number.
Next you must create a new list just
like the previous one but eliminating 
duplicate numbers. Show this second list 
to verify that we have removed the duplicates.
'''

list=[]
list2=[]
boolean=True

while boolean==True:
    num=int(input("Enter a number: "))
    if num >= 0:
        list.append(num)
    else:
        boolean=False


for i in list:
    if i not in list2:
        list2.append(i)

   
print(list)
print(list2)
