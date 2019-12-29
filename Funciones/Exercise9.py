#Exercise9

'''
We will create a program to work with a stack. 
A stack is a data structure that allows us to
save a set of variables. The fundamental
characteristic is that the last element that is
added to the set is the first that can be removed.

To represent a stack we will use a list of character strings.

We will create several functions to work with the stack:

Battery Length: Function that receives a
battery and returns the number of items it has.

This Empty Battery: Function that receives a
battery and returns if the battery is empty,
has no elements.

It is Full Battery: Function that receives
a battery and returns if the battery is full.

Add Stack: function that receives a string of
characters and a stack, and adds the string to
the stack, if it is not full. If it is full it
shows an error message.

Remove From Battery: A function that receives
a battery and returns the last item added and
deletes it from the battery. If the battery is
empty it shows an error message.

Write Battery: Function that receives a battery
and displays the battery elements on the screen.

Make a main program that allows us to use the
previous functions, which shows us a menu,
with the following options:

Add item to the stack

Remove item from battery

Battery length

Show battery

Leave
'''

#@CarlosAntonio


stack=["Carlos","Jhony","Lupita","Ariel"]

def length(stack):
    return len(stack)

def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False

def isFull(stack):
    if len(stack)==4:
        return True
    else:
        return False

def addElement(str,stack):
    if isFull(stack)==True:
        return "Stack is full"
    else:
        stack.append(str)

def takeOut(stack):
    if isEmpty==True:
        return "Stack is empty"
    else:
        return stack.pop()

def showStack(stack):
    print(stack)


print(length(stack))
print(isEmpty(stack))
print(isFull(stack))
print(addElement("Juan",stack))
print(takeOut(stack))
print(showStack(stack))

