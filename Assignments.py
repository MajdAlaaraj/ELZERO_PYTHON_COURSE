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
# admins=["Ahmad","Mohamad","Majd","Younes","Osama","Hasan","Enas","Sameh"]    
# #Login
# name = input("Please Type Your Name :").strip().capitalize()
# if name in admins :
#     print(f"Hello {name} Welcome Back")
#     option = input("Delete Or Update ? ").strip().capitalize()
# #Update Option    
#     if option == "Update" :
#         theNewName=input("Type The New Name Please : ").strip().capitalize()
#         admins[admins.index(name)]=theNewName
#         print("The Name Updated.")
# #Delete Option        
#     elif option == "Delete" :
#             admins.remove(name)
#     else : print("Sorry , You Typed Wrong Option Try Again.")


# else : 
#     print("You Are Not Admin")
#     status = input("Do You Want To Be An Admin ?(y/n)").strip().capitalize()
#     if status == "Yes" or status == "Y" :
#         admins.append(name)
#         print("You Are An Admin Now.")
#     else : print("Thank You.") 

#________________________________________________
#(3) Simple Bookmark Manager 
#________________________________________________   
# Empty List To Fill It 
# myWebSites = []
# # Maximum Web Sites Allowed
# maximum = 5
# # Input The New Website
# while maximum > 0 :
#     web = input("Web Site Name Without https://")
#     # Add The Website To The List
#     myWebSites.append(f"https://{web.strip().lower()}")
#     # Decrease 1 From The Allowed Websites
#     maximum-=1
#     print(f"Website Added , {maximum} Places Left")
#     print(myWebSites)
# else : 
#     print("The Bookmark Is Full , You Can\'t Add More.") 
# #Check The List Is Not Empty 
# if len(myWebSites) > 0 :
#     # Sort The List
#     myWebSites.sort()
#     # Printing The List 
#     index = 0
#     print("The List Of The WebSites Is : ")
#     while index < len(myWebSites) :
#         print(myWebSites[index])
#         index+=1

#________________________________________________
#(4) Simple Password Guess 
#________________________________________________
# tries = 4

# mainPassword = "glory"

# inputPassword = input("Enter The Password Please : ")

# while inputPassword != mainPassword :
#     tries-=1
#     print(f"Wrong Password , {'last' if tries == 0 else tries} Chance left.")
#     inputPassword = input("Enter The Password Please : ")
#     if tries == 0 :
#         print("All Tries Is Finish.")
#         break

# else : 
#     print("Correct Password")
#________________________________________________
#(5) Speed Test
#________________________________________________

# from time import time 
# def speedTest(func):
#     def wrapper():
#         start = time()
#         func()
#         end = time()
#         print(f"The function take about {end - start} sec.")
#     return wrapper

# @speedTest
# def loop () :
#     for num in range(1,10000) :
#         print(num)

# loop()

#________________________________________________
#(6) Loop on many Iterators with zip()
#________________________________________________
# list1 = [1,2,3,4,5]
# list2 = ["A","B","C"]
# tuple1 = ("man","woman","girl","boy")
# dict1 = {"name":"majd","age":"28" ,"tall":"173"}

# for item1,item2,item3,item4  in zip(list1,list2,tuple1,dict1) :
#     print("list1 item =>" ,item1)
#     print("list2 item =>" ,item2)
#     print("tuple1 item =>" ,item3)
#     print("dict1 key =>" ,item4 ," | dict1 value =>" ,dict1[item4])

#________________________________________________
#(7) Image manipulation with pillow 
#________________________________________________

# from PIL import Image
# # open image 
# img = Image.open(r"D:\ritrica\PicsArt_06-07-12.57.54.png")
# # image show 
# # img.show()
# # crop image 
# # first we detect the crop field 
# w,h = img.size
# myBox = (0,0,h,w/2)
# # second we give the crop field as a parameter o the crop func.
# newImg = img.crop(myBox)
# # newImg.show()

# newimg1 = img.crop(myBox)
# newimg1.show()

#________________________________________________
#(8) Exceptions handling advanced example.
#________________________________________________
# we create a while loop to try open a file with 5 tries ,if the user write the file name 
# correctly the file open else , if the tries is out it print sorry your tries is out.  

# file = None
# tries = 5 
# while tries > 0 :
#     try:
#         print (f"You have {tries} tries left.")
#         print("Enter the file name with the absolute path.")
#         print(r"Example: D:\programmes\file.txt")
#         file_name = input("Enter the file name => ").strip()
#         file = open(file_name, "r")
#         print(file.read())
#         break 
#     except FileNotFoundError :
#         print("The file not found.")
#         tries-=1
#     except :
#         print("Error happened.")
#     finally :
#         if file is not None :
#             file.close()
#             print("File closed.")
# else :
#     print("Sorry you dont have any tries.")



















