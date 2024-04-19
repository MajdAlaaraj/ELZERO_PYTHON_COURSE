#Assignment 1
import os
for i in range(1,51) :
    if i == 25 :
        file = open(rf"C:\Users\Dell\Desktop\Python\special-text.txt","w")
        file.writelines(os.getcwd())
        file.write("\n")
        file.writelines(os.path.dirname(os.path.abspath(__file__)))
        file.write("\n")
        file.writelines(os.path.abspath(__file__))
        file.close()
    else :    
        file = open(rf"C:\Users\Dell\Desktop\Python\txt{i}.txt","w")
        file.write(f"Elzero Web School => {i}\n")
        file.close()
#Assignment 2            
file = open(rf"C:\Users\Dell\Desktop\Python\txt1.txt","a")
for i in range(50) :
    file.write("Appended => Elzero Web School\n")
file.close

#Assignment 3 
file = open(rf"C:\Users\Dell\Desktop\Python\txt1.txt","a")

