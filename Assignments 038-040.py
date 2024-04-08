#Assignment 1
name=(input("please enter your name : ")).strip()
print(f"Hello {name.capitalize()}, Happy To See You Here.")

#Assignment 2
age=int(input("Enter Your Age : "))
if age<16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else :
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")    

#Assignment 3
first_name=input("What\'s Your First Name : ").strip().capitalize()
second_name=input("What\'s Your Last Name : ").strip().capitalize()
print(f"Hello {first_name} {second_name[0]}.")

#Assignment 4
email=input("Please Enter Your Email : ").strip().lower()
name=email[:email.index("@")].capitalize()
provider=email[email.index("@")+1:email.index(".")]
domain=email[email.index(".")+1:]
print(f"Your Name Is {name}")
print(f"Email Service Provider Is  {provider}")
print(f"Top Level Domain Is {domain}")


