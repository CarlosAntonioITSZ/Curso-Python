#Exercise8
'''
Write two functions that allow you to calculate:

The number of seconds in a given time in hours,
minutes and seconds.

The number of hours, minutes and seconds of
a given time in seconds.

Write a main program with a menu where you can
choose the option to convert to seconds,
convert to hours, minutes and seconds or exit the program.
'''
#@CarlosAntonio

def seconds (hours, minutes, secondsT):
    hS=hours*3600
    mS=minutes*60
    secondsT+=hS+mS

    return secondsT

def hms (secondsT):
    h=secondsT//3600
    m=(secondsT-(h*3600))//60
    s=(secondsT-(h*3600))-(m*60)
    return h,m,s

print("")
print("-------------------------------------------")

print("1.- The number of seconds in a given time\n    in hours,minutes and seconds")
print("")
print("2.- The number of hours, minutes and \n    seconds of a given time in seconds.")
print("")
print("3.- Exit")
print("-------------------------------------------")

print("")

try: 
    option=int(input("Enter a option: "))

    if option==1:
        print(seconds(10,50,40))
    elif option==2:
        print(hms(700000))
    elif option==3:
        print("Bye")
    else:
        print("la opcion no existe ")

except ValueError:
    print("It´s not a number")