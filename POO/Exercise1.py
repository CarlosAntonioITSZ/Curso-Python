#Exercise1
'''
We are going to create a class called Person.
Its attributes are: name, age and ID.
Build the following methods for the class:

A constructor, where the data may be empty.

The setters and getters for each of the attributes.
You have to validate the data entries.

show (): Shows the person's data.

esMayorDeEdad (): Returns a logical value
indicating if it is of legal age.
'''
#@CarlosAntonio

class Person():
    
    def __init__(self,name,age,dni):
        self.__name=name
        self.__age=age
        self.__dni=dni
    
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name=name

    def getAge(self):
        return self.__age
    
    def setAge(self,age):
        self.__age=age

    def getDni(self):
        return self.__dni
    
    def setDni(self,dni):
        self.__dni=dni

    def show(self):
        print("----------------------------")
        print("Name: ",self.__name,"\nAge: ",self.__age,"\nDni: ",self.__dni)
        print("----------------------------")
        
    def isOlder(self):
        if self.__age>=18:
            return True
        else:
            return False

p1=Person("Carlos",20,"AOJ12330CJAL")

try:
    p1.setAge(g)
except NameError:
    print("Try again")

p1.show()
print(p1.isOlder())

print("")

p2=Person("Juan",16,"ASFDJ12330CJAL")
p2.setAge(17)
p2.show()
print(p2.isOlder())