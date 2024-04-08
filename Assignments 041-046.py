#Assignment 1
num1=int(input("Enter The First Number: ").strip())
num2=int(input("Enter The Second Number: ").strip())
operation=input("Please Enter The Operation (+ , - , * , / ,%) : ").strip()
if operation=="+":
    print("The Result Is : ",num1+num2)
elif operation=="-":
    print("The Result Is : ",num1-num2)
elif operation=="*":
    print("The Result Is : ",num1*num2)
elif operation=="/":
    print("The Result Is : ",num1/num2) 
elif operation=="%":
    print("The Result Is : ",num1%num2)  
else: print("The Operation Is Wrong,Please Try Again. ")   

#Assignment 2
age = 17
print("App Is Suitable For You"if age>16 else "App Is Not Suitable For You")

#Assignment 3
age = int(input("Enter Your Age : ").strip())
if age<10 or age > 100 :
    print ("Your Age Is Out Of Range. ")
months = age * 12
weeks = months * 4
days = age * 365 
hours = days * 24 
minutes = hours * 60
seconds = minutes * 60
print("Your Age In Units Is :")
print(f"{months} Months .")
print(f"or {weeks} weeks.")
print(f"or {days} days.")
print(f"or {hours} hours.")
print(f"or {minutes} minutes.")
print(f"or {seconds} seconds.")

#Assignment 4
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
country = input("Input Your Country : ").capitalize().strip()
price = 100
discount = 30
if country in countries :
    print("Your Country Eligible For Discount And The Price After Discount Is $70")
else : 
    print("Your Country Not Eligible For Discount And The Price Is $100")    