#Exercie5

''''
Create an application that allows you to guess a number. 
The application generates a random number from 1 to 100. 
Next it asks for numbers and answers 
if the number to be guessed is greater or less than the one entered, 
in addition to the remaining attempts (you have 10 attempts to get it right). 
The program ends when the number is correct 
(it also tells you how many attempts you have made it right), 
if you reach the limit of attempts it shows you the number that you had generated
'''

#@CarlosAntonio

from random import randint

randomNumber=randint(1,100)
 
attempts=1

while attempts<11:

    number=int(input("Enter a number: "))

    if number>randomNumber:
        print("the number is greater")
        attempts+=1

    elif number<randomNumber:
        print("the number is less")
        attempts+=1
    
    print("")#Space
    
    if attempts==11:
        print("You lost, the number is ",randomNumber)

    if number==randomNumber:
        print("You win, number of attemps: ",(10-attempts))
        break
