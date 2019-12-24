#Exercise4

'''
Enter a string of characters and indicate
if it is a palindrome. 
A palindrome word is one that reads 
the same way ahead as it does back.
'''

#@CarlosAntonio

word=input("Enter a word: ")

if word==word[::-1]:
    print("\n",word[::-1])

print("\nFinished")