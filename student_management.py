Student_name = input("enter student name: ")
Age = int(input("Enter your Age:"))
Roll_number=int(input("Enter your roll number:"))
course_name=input("Enter your course name: ")

subject =["Computer Science","English","Math","Science","Urdu"]
subject.append("SST")
subject.remove("Urdu")
print("subject:",subject)
grades = ("A", "B", "A+", "B+")

print("Grades:",grades)
print("total subject:",len(subject))
