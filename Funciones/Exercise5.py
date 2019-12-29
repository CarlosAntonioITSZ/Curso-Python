#Exercise5
'''
Create a subroutine called "Login",
which receives a username and password and returns 
you True if the username is "user1" and the password is "asdasd". 
It also receives the number of attempts
that were attempted to login and if it was 
not possible to login, increase this value.
Create a main program where you ask for a username
and password and try to login, we only have three opportunities to try.
'''
#@CarlosAntonio

def login(user,password):
    if user=="user1" and password=="asdasd":
        return True
    else:
        return False
     
cont=0
while cont<3:   
    user=input("Enter a user: ")
    password=input("Enter a password: ")
    if login(user,password)==True:
        print("Welcome to the system")
        break
    elif cont==2:
        print("You have made too many attempts")
        print("")
        cont+=1
    else:
        print("Try again")
        cont+=1
        print("")