
# Question 1: Personal Information
# Create a program that takes the following information from the user:
# 1. Name
# 2. Age
# 3. City
# 4. Education
# Requirements:
# - Print the name in uppercase.
# - Add 5 to the age and print the result.
# - Print the city in lowercase.
# - Find and print the length of the name.


name = input("Enter your Name:")
age=int(input("Enter your Age: "))
city=input("Enter City name:")
education=input("Enter your Education:")
print("Name iS:",name.upper())
print("Age:",age+5)
print("City:",city.lower())
print("Eduation:",education)
print("Name Length:",len(name))


# Question 2: Shopping List
# Create a list:
# shopping = ["Milk", "Bread", "Eggs", "Butter"]

# Tasks:
# 1. Add "Rice" to the list.
# 2. Remove "Bread" from the list.
# 3. Replace "Eggs" with "Chicken".
# 4. Count the total number of items.
# 5. Print the updated list.

shopping = ["milk","bread","eggs","butter"]
shopping.append("rice")
shopping.remove("bread")
shopping[1]="chicken"
print("Total item in list:",len(shopping))
print(shopping)


# Question 3: Student Marks
# Take marks for three subjects from the user:
# 1. English
# 2. Math
# 3. Computer
# Requirements:
# 1. Take marks for each subject using input().
# 2. Convert the marks into integers.
# 3. Store all three marks in a list.
# 4. Calculate the total marks.
# 5. Print the marks list and the total marks.

english=int(input("Enter English subject marks:"))
math=int(input("Enter Math subject marks: "))
computer=int(input("Enter Computer subject marks:"))
marks=[english,math,computer]
total_marks = sum(marks)
print("Marks list:",marks)
print("Total marks in Subject:",total_marks)



#Question 4: Tuple Practice
# Create a tuple:
# languages = ("Python", "Java", "C++", "JavaScript")
# Requirements:
# 1. Print the first language.
# 2. Print the last language.
# 3. Count the total number of languages.
# 4. Check whether "Python" is available in the tuple.

languages = ("Python", "Java", "C++", "JavaScript")
print("First language:",languages[0])
print("Last language:",languages[-1])
print("Total language:",len(languages))
print("Python" in languages)


