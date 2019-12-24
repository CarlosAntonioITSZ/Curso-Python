#Exercise1

'''
Assuming that we have entered a string by keyboard
that represents a phrase (words separated by spaces), 
make a program that counts how many words it has.
'''

#@CarlosAntonio

phrase=input("Enter a phrase: ")
words=1

for i in phrase:
    if i==" ":
        words+=1

print("\nNumbers of words: ",words)