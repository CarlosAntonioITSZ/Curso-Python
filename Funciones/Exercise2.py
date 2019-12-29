#Exercise2
'''
Create a "ConvertSpaced" function, which receives
a text as a parameter and returns a string with
an additional space after each letter. 
 
For example,
"Hello, you" will return "H o l a, t ú". 
Create a main program where this function is used.
'''
#@CarlosAntonio

def convertSpaced (string):
    for i in string:
        print(i,end=" ")

string=input("Enter a string: ")

convertSpaced(string)
