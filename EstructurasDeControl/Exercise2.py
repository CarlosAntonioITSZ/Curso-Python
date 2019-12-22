#Exercise2
'''
Algorithm that asks for three numbers
and the ordered examples (from highest to lowest);
'''
#@CarlosAntonio

print(" ")
one=int(input("Enter a number: "))
two=int(input("Enter a number: "))
three=int(input("Enter a number: "))
print("")

if one > two and one > three:
    if two > three:
        print(one, two, three)
    else:
        print(one, three, two)
elif two > one and two > three:
    if one > three:
        print(two, one, three)
    else:
        print(two, three, one)
elif three > one and three >two:
    if one > two:
        print(three, one, two)
    else:
        print (three, two, one)
print(" ")