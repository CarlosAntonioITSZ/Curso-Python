'''
We are going to create a python program 
where we are going to declare a dictionary 
to save the prices of the different fruits. 

The program will ask for the name of the fruit 
and the quantity that has been sold and will show 
us the final price of the fruit from the data 
stored in the dictionary. If the fruit does 
not exist it will give us an error. 
'''
fruits={}

for i in range(1,7):
    key=input("Enter a fruit: ")
    price=int(input("Enter a price: "))
    fruits[key]=price
    print("")


    fruit=input("Enter a fruit to look for: ")
    quantity=int(input("Enter a quantity sold: "))

    priceFinal=fruits[fruit]*quantity
    print(priceFinal)

    


print(fruits)