#Student record using tuple
student_record = (53,"Mozma Abid",889)
roll_no,name,marks= student_record
print(f"Student Roll no:{roll_no}\nStudent Name:{name}\nStudent Marks:{marks}")


#use a list comprenshion [7,14,...,70]
table=[7*i for i in range(1,11)]
print(table)


#make copy or not
a=[1,2,3,4]
b = a
c=a.copy()
a.append("5")
print(a)
print(b)
print(c)