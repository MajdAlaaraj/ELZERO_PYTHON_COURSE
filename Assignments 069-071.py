#Assignment 1
#if any value in variable values is true the the condition will be true.
values = (0, 1, 2)

if any(values):

    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]
# #the condition will be true if one of three at least is true 
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

    print("Good")

else:

    print("Bad")


#The result is Good

#Assignment 2

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  


#Assignment 3

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

    print("Good")

#Assignment 4
def my_all(list) :
    for item in list :
        if not item :
            return False
    return True

def my_any (list) :
    for item in list :
        if item :
            return True
    return False    

def my_min(list) :
    min = list[0]
    for item in list :
        if item < min :
            min = item 
    return min 

def my_max(list) :
    max = list[0]
    for item in list :
        if item > max :
            max = item 
    return max


print(my_all([1, 2, 3]))
print(my_all([1, 2, 3, []]))

print(my_any([0, 1, [], False]))
print(my_any([(), 0, False])) 


print(my_min([10, 100, -20, -100, 50])) 
print(my_min((10, 100, -20, -100, 50)))

print(my_max([10, 100, -20, -100, 50, 700])) 
print(my_max((10, 100, -20, -100, 50, 700)))













