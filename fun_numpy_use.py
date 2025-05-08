import numpy as np

data_type = [('name','S15'),('height',float),('class',int)]

names = []
hieghts = []
classes = []

n = int(input("enter the no.of students: "))

for i in range(n):
    x=input(f"\n enter the name off student{i+1}: ")
    y=input("enter the class")
    z=float(input("enter the hieght"))

    names.append(x.encode())
    classes.append(y)
    hieghts.append(z)

students = np.zeros(n,dtype=data_type)

students['name']=names
students['class']=classes
students['height']=hieghts

print("\n original array")
print(students)

print("\n sorted array")
sorted_students=np.sort(students,order='hieght')
print(sorted_students)


