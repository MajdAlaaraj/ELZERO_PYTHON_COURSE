# Assignment 1
def calculate(num1 ,num2,operator = "add"):
    if operator.lower() == "add" or operator.lower()=="a" :
        return num1+num2
    elif operator.lower() == "subtract" or operator.lower()=="s" :
        return num1-num2
    elif operator.lower() == "multiply" or operator.lower()=="m" :
        return num1*num2
    else :
        return "The Operation Is Wrong."

num1 = int(input("Enter The First Number :"))
num2 = int(input("Enter The second Number :"))
op = input("Please Enter The Operation :")

print (calculate(num1,num2,op))


# Assignment 2
def addition (*nums) :
    sum = 0
    for num in nums :
        if num == 10 :
            continue
        elif num == 5 :
            sum = sum-5
        else :
            sum = sum + num
    return sum     

print (addition(100,100,5,5))


#Assignment 3
def show_skills(name ,*skills ) :
    if len(skills)==0 :
        print(f"Hello {name} You Have No Skills To Show")
    else :    
        print(f"Hello {name} Your Skills Are :")
        for skill in skills :
            print (f"- {skill}")


show_skills("ahmad" ,"python")        



#Assignment 4 

def say_hello(name="Unknown" ,age="Unknown" , country="Unknown"):
    print(f"Hello {name} Your Age Is {age} and you live in {country}")


say_hello("majd", 28 ,"syria")
say_hello("ahmad")
say_hello()
    
