#Exercise 8
'''
A seller receives a base salary plus an extra 10% 
for commission of his sales, the seller wants 
to know how much money he will get for commissions
for the three sales he makes in the month and the 
total he will receive in the month taking into 
account his salary base and commissions.
'''

#@CarlosAntonio

salary=float(input("Enter the salary: "))

commission=salary*.10

finallySalary=salary+(commission*3)

print(f"The finally salary is {finallySalary}")