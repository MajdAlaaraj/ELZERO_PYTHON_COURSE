#(1) Numbers Guessing Game 
import random
rand_num = random.randrange(1,10)
Guess = int(input("Please Guess A Number between 1=>10 : "))
while rand_num!= Guess :
    if Guess > rand_num :
        print("Too High")
        Guess=int(input("Please Enter A number Again :"))
    elif rand_num < Guess :
        print("Too Low ")
        Guess = int(input("Please Enter A number Again :")) 
    else :
        break
print ("Your Guess is Right.")        

#(2) 
