#Exercise5

'''
Write a program that implements a phonebook. 
Names and phone numbers may be stored in the phonebook. 
The program will give us the following menu:

Add / modify: Ask us for a name. If the name
is in the phonebook, you must show the phone and,
optionally, allow it to be modified if it is 
not correct.
If the name is not found, you must enter 
the corresponding phone number

Search: It asks us for a string of characters,
and shows us all contacts whose names begin 
with that string.

Delete: It asks us for a name and if it exists
it will ask us if we want to delete it from the agenda.

List: Shows all contacts in the phonebook.

Implement the program with a dictionary.
'''

#@CarlosAntonio

phonebook={"Carlos":2727197131,"Carla":2727197531,"Cuco":2727197131,"Lupita":272329711,"Ariel":2754197131}


print("-----Menu-----")
print("1.- Add/Modify")
print("2.- Search")
print("3.- Delete")
print("4.- Show")
print("5.- Exit")
print("-------------")

cond=True

while cond==True:

    option=int(input("Enter a option: "))
    print("")

    if option==1:
        name=input("Enter a name: ")
        if name not in phonebook:
            number=int(input("Enter a number: "))
            phonebook[name]=number
            
        elif name in phonebook:
            print ("Number: ",phonebook[name])
            answer=input("Do you want to change the number? S/N: ")

            if answer=="S":
                newNumber=int(input("Enter a new number: "))
                phonebook[name]=newNumber
                print ("New number: ",phonebook[name])

            else: 
                print("Number not updated")
                print("")

        print("")        
    elif option==2:
        initial=input("Enter a string: ")
        print("")
        for nombre, numero in phonebook.items():
            if nombre.startswith(initial):
                print("")
                print("%s  %s" % (nombre,phonebook[nombre]))

    elif option==3:
        nameS=input("Enter a name: ")
        if nameS in phonebook:
            opt=input("Do you want to remove the contact from the list? S/N: ")
            if opt=="S":
                phonebook.pop(nameS)
                print("Contact removed")
               
            else:
                print("")
        else:
            print("Contact not found")
        print("")

    elif option==4:
        print("----Phonebook----")
        for i in phonebook:
            print(i,phonebook[i])
        print("-----------------")
    else:
        cond=False
    print("")
    