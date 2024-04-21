#Assignment 1
def remove_chars(string):
    return string[1:-1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars,friends_map )

for name in cleaned_list :
    print(name)
    
#Lambda function :
for name in map(lambda string :string[1:-1] ,friends_map) :
    print(name)

#Assignment 2 

def get_names(name) :
    return name.endswith("m")

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names,friends_filter)

for name in names :
    print(name)


#Assignment 3
from functools import reduce

def multi(num1,num2):
    return num1*num2

nums = [2, 4, 6, 2]

multiple = reduce(multi,nums)
print(multiple)


#Assignment 4 

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
my_skills = enumerate(reversed(skills) ,50)

for counter ,skill in my_skills :
    if type(skill) == type(1):
        continue
    else :
        print(f"{counter} _ {skill}")
