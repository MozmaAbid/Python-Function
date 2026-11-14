
#multi line string
print( """My name is \"Mozma Abid\".
I am computer science graduation from government sadiq college women usniversity.
I am interested in web development""")


#string length
txt = "  Hello World!"
print("string length:",len(txt))
# slicing
print("Slicing Method:")
print(txt[2:6])
print(txt[0:13])

# #negative indexing
print("Negative Indexing Method:")
print(txt[-13:-10])
print(txt[-8:-3])

#string method

print("capitalize the string:" ,txt.upper())
print("Small the string:",txt.lower())
print("Replace H with F:" ,txt.replace('H','F'))
print("Remove start and ending space:",txt.strip())
print("Split the string:" ,txt.split(" , "))

#string format
print ("String format ")
name = "python"
print("I am start {} learning".format(name))
print(f"I am start {name}learning ")

#String Concatenation 


a = "New"
b = "Class"
print("Combine two string:",a+b)

