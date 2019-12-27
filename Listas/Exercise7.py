#Exercise7

'''
Write a program that allows you to create 
a list of words and that, following three options:

Count: He asks me for a chain, 
and tells me how many times it appears on the list

Modify: It asks me for a chain, and another 
chain to modify, and modifies all the occurrences
of the first by the second in the list.

Delete: It asks me for a string, and removes 
it from the list.

Show: Shows the list of strings

Finish
'''

#@CarlosAntonio
answerS=True
list=[]

while answerS==True:
    appened=input("Enter a string: ")
    if not appened.isdigit():
        list.append(appened)
    else:
        answerS=False
print("----------------")
print("1. Count")
print("2. Modify")
print("3. Delete")
print("4. Show")
print("--------------")

answerS=int(input("Enter a option: "))
print("")

if answerS==1:
    str=input("Enter a string: ")
    print(list.count(str))
elif answerS==2:
    print(list)
    str=input("Enter a new string: ")
    str2=input("Enter a old string: ")
    
    list.insert(list.index(str2),str)
    list.remove(str2)
    print(list)
elif answerS==3:
    str=input("Enter a string: ")
    list.remove(str)
    print(list)
elif answerS==4: 
    print(list)
else:
    ("Error")