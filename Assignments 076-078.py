#Assignment 1

import random
rand = random.randrange(10,50)
while True :
    even_rand = random.randrange(2,10)
    if even_rand % 2 == 0 :
        break

while True :
    odd_rand = random.randrange(1,9)
    if odd_rand % 2 != 0 :
        break
print(f"Random Number Between 10 And 50 => {rand}")

print(f"Random Even Number Between 2 And 10 => {even_rand}")

print(f"Random Odd Number Between 1 And 9 => {odd_rand}")

print(dir(random))

#Assignment 2 

main.py
import sys
sys.path.append(r"C:\Users\Dell\Desktop\python")
import my_mod

my_mod.say_hello("Majd")
my_mod.say_welcome("MAJD")


my_mod.py

def say_hello (name):
    print(f"Hello {name}")

def say_welcome(name) :
    print(f"Welcome {name}")


#Assignment 3

from my_mod import say_welcome

say_welcome("MAJD")

#Assignment 4 

from my_mod import say_welcome as new_welcome


new_welcome("MAJD")

