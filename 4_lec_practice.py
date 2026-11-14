
name = "Mozma Abid"


#check the type
print(name,"\t", type(name))

#check length
print(len(name))  

#convert the type and use escape sequence
percentage = 80.9
print(percentage ,"\t",type(percentage))
percentage = int(percentage)
print(percentage ,"\t", type(percentage))

#list
Games =["football", "cricket" , "hockey" , "basketball" , "tabletennis"]
print("Games Name: " , Games)

#use random modules
import random
Games = random.choice(Games)
print("Random Select One Game we play: " , Games)

#Dict
players = {
    "runs" : 50,
    "Game" :"cricket",

}
print(players)


