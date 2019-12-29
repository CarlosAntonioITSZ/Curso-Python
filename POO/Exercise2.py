#Exercise2

'''
Create a class called Account that will have the
following attributes: holder (who is a person)
and quantity (can have decimals).
The holder will be mandatory and
the amount is optional.
Build the following methods for the class:

A constructor, where the data may be empty.

The setters and getters for each of the attributes.
The attribute cannot be modified directly,
only by entering or withdrawing money.

show (): Shows the account information.

enter (amount): an amount is entered into
the account, if the amount entered is negative, nothing will be done.

'''

#@CarlosAntonio

class Account():
    def __init__(self,headline, quantity=0):
        self.__headline=headline
        self.__quantity=quantity
    
    def getHeadline(self):
        return self.__headline

    def setHeadline(self,h):
        self.__headline=h

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self,q):
        self.__quantity=q

    def show(self):
        return str(self.__headline),"",str(self.__quantity)

    def deposit(self,q):
        if q<0:
            print("nothing")
        else:
            self.__quantity+=q
    
    def withdrawals(self,q):
        self.__quantity-=q

'''
c=Account(["Carlos",21,"Orizaba"],100)

while True:
    opt=int(input(": "))

    if opt==1:
        q=int(input("Enter a quantity: "))
        c.deposit(q)
    elif opt==2:
        q=int(input("Enter a quantity: "))
        c.withdrawals(q)
    elif opt==3:
        c.show()
    else:
        break
'''
class YoungAccount(Account):
    
    def __init__(self,h,q,bonus):
        super().__init__(h,q)
        self.__bonus=bonus

    def isAValidHolder(self):
        pass

    def show(self):
        return super().show(),"", str(self.__bonus)

    def isValid(self):
        if 

c1=YoungAccount(["Carlos",21,"Orizaba"],100,4)
print(c1.show())
