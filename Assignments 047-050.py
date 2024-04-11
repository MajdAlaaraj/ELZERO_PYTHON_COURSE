#Assignment 1
num = int(input("Please Enter Number :"))
count = 0
if num <= 0 :
    print("The Number Equal Or Less Than 0.")
while num > 0 :
    if num == 1 : break
    print(num-1)
    num-=1
    count+=1
print(f"{count} Number Printed Successfully")   

#Assignment 2
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
count = 0 
index = 0
while index < len(friends):
    if friends[index][0].islower() :
        count+=1
    else : 
        print(friends[index])
    index+=1    
print(f"Friends Printed And Ignored Names Count Is {count}")            

#Assignment 3 
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills :
#     print(skills[])



#Assignment 4

my_friends = []

max = 4 
while max > 0:
    name = input("Please Type A Name To Insert It : ")
    if name.isupper() : 
        print("Invalid Name")
    elif name.islower() and max > 0 :
        max -=1
        name = name.capitalize()
        my_friends.append(name.strip())
        print(f"Friend {name} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {max}")
    elif name ==name.capitalize() and max > 0:
        my_friends.append(name.strip())
        print(f"Friend {name} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {max}")
print(f"The Name Of Your Friends Is : {my_friends}")





        
