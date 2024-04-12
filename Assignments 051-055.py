# Assignment 1 
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
counter = 1

for num in my_nums :
    if num % 5 == 0 :
        print(f"{counter} => {num}")
        counter+=1
else: 
    print("All Numbers Printed.")    

# Assignment 2
for num in range(1,21):
    if num == 6 or num ==8 or num == 12 :
        continue
    print(str(num).zfill(2))
else :
    print("All Number Printed.") 
#Assignment 3
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
total = 0
for subject , grade in my_ranks.items():
    if grade=="A":
        print(f"My Rank in {subject} Is A And This Equal 100 Points")
        total+=100
    elif grade=="B":
        print(f"My Rank in {subject} Is B And This Equal 80 Points") 
        total+=80  
    elif grade=="C":
        print(f"My Rank in {subject} Is C And This Equal 40 Points")
        total+=40     
else : 
    print(f"Total Point Is {total}")        

#Assignment 4
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
A=100
B=80
C=40
D=20
for name in students :
    print  ("-"*30)
    print  (f"--Student Name => {name}")
    print  ("-"*30)
    total = 0
    for sub , grade in students[name].items() :
        if grade=="A":
            print(f"-{sub} => {A} points.")
            total+=A
        elif grade =="B" :
            print(f"-{sub} => {B} points.")
            total+=B
        elif grade =="C" :
            print(f"-{sub} => {C} points.")
            total+=C
        elif grade =="D" :
            print(f"-{sub} => {D} points.")
            total+=D    
    print(f"Total Points For {name} Is {total}")