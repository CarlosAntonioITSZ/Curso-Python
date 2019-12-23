#Exercise7

'''
Algorithm that asks for characters 
and prints 'it's a vowel' if they are vowels 
and 'it's not a vowel' otherwise, 
the program ends when a space is entered.
'''

#@CarlosAntonio

vowels='aeiou'
notVowels='bcdfghjklmnñpqrstuvwxyz'
character=''

while character!=" ":
    character=input("Enter a character: ").lower()
    if character in vowels:
        print("it's a vowel")
        print("")
    elif character in notVowels:
        print("it's not a vowel")
        print("")
    elif character not in vowels and character not in notVowels and character!= " ":
        print ("invalid character")
        print("")