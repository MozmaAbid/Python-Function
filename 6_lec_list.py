#List Method
language=["python","c","c++","oop"]
print(language)


#append method
language.append("javascript")
print(language)


#insert method
language.insert(1,"javascript")
print(language)

#pop method
language.pop(5)
print(language)

#Remove method
language.remove("c")
print(language)


#del method
del language[0]
print(language)


#nested list
language=["python","c","c++","oop",["Begnier level","intermediate level","Advance level"]]
print(language[0],language[4][0])

