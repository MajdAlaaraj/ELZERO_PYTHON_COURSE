#______________________________________________
#(1) calculate your age
# _____________________________________________
age=int(input("What\'s Your Age ?").strip())
time_unit=input("please Enter Time Unit(Months/M _Weeks/W _Days/D) :").strip().capitalize()
months=age*12
weeks=months*4
days=age*365
if time_unit == "Month" or time_unit == "M" :
    print(f"Your Age In Months Is {months}")
elif time_unit == "Weeks" or time_unit == "W" :
    print(f"Your Age In Weeks Is {weeks}")
elif time_unit == "Days" or time_unit == "D" :
    print(f"Your Age In Days Is {days}") 
else :
    print("Your Input Is Wrong, Please Try Again. ")       
#________________________________________________
#(2) Practical Membership Control
#________________________________________________
# The name of people who allow to enter the system 
admins=["Ahmad","Mohamad","Majd","Younes","Osama","Hasan","Enas","Sameh"]    
#Login
name = input("Please Type Your Name :").strip().capitalize()
if name in admins :
    print(f"Hello {name} Welcome Back")
    option = input("Delete Or Update ? ").strip().capitalize()
#Update Option    
    if option == "Update" :
        theNewName=input("Type The New Name Please : ").strip().capitalize()
        admins[admins.index(name)]=theNewName
        print("The Name Updated.")
#Delete Option        
    elif option == "Delete" :
            admins.remove(name)
    else : print("Sorry , You Typed Wrong Option Try Again.")


else : 
    print("You Are Not Admin")
    status = input("Do You Want To Be An Admin ?(y/n)").strip().capitalize()
    if status == "Yes" or status == "Y" :
        admins.append(name)
        print("You Are An Admin Now.")
    else : print("Thank You.") 

#________________________________________________
#(3) Simple Bookmark Manager 
#________________________________________________   
# Empty List To Fill It 
myWebSites = []
# Maximum Web Sites Allowed
maximum = 5
# Input The New Website
while maximum > 0 :
    web = input("Web Site Name Without https://")
    # Add The Website To The List
    myWebSites.append(f"https://{web.strip().lower()}")
    # Decrease 1 From The Allowed Websites
    maximum-=1
    print(f"Website Added {maximum} Places Left")
    


























