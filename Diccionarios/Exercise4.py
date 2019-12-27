#Exercise4

'''
Encode a program in python that 
allows us to save the names of students
in a class and the grades they have obtained.
Each student can have different amount of grades. 
Save the information in a dictionary
whose keys will be the names of the 
students and the values ​​will be ready
with the notes of each student.

The program will ask for the number of
 students that we are going to introduce, 
 will ask for their name and will ask for 
 their notes until we enter a negative number. 
 At the end the program will show us the 
 list of students and the average grade 
 obtained by each one of them. Note: 
 
 if you enter the name of a student who 
 already exists the program will give us an error.
'''

#@CarlosAntonio

students={}

n=int(input("Number of students: "))

for i in range (0,n):
    print("----Student",(i+1),"----" )
    name=input("Enter a name: ")
    if name not in students:
    #-------------------------------------
        grades=[]
        cal=int(input("Enter grades: "))
        while cal>=0:
            grades.append(cal)
            cal=int(input())
    #-------------------------------------
   
        students[name]=grades.copy()
    else:
        print("El alumno ya existe")
        
    print("------------------" )

print("Students: ",students)
print("")
for a, n in students.items():
    print("%s has taken half note %f" % (a,sum(n)/len(n)))