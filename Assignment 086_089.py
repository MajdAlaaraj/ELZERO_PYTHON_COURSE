#Assignment 1 
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

final_string = ""

for data in zip(my_list, my_tuple):
    for item in data:
        if isinstance(item, str):
            final_string += item

print(final_string)  # Output: Elzero

#Assignment 2
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2] 
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

final_string = ""

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if isinstance(item1, str) and isinstance(item2, str) and isinstance(item3, str):
        if item1 != item2 and item1 != item3 and item2 != item3 :
            final_string += item1 + item2 + item3

print(final_string)  # Output: Elzero

#Assignment 3
from PIL import Image
my_image = Image.open(r"C:\Users\Dell\Downloads\elzero-pillow.png")
letter_l = (400,0,800,400)
image_l =my_image.crop(letter_l)
gray_image = image_l.convert("L")
gray_image.show()
second_row = (0,400,1200,800)
image2 = my_image.crop(second_row)
rotate_image = image2.rotate(180)
gray_rotate_image = rotate_image.convert("L")
gray_rotate_image.show()

# my_image2 = image_l.save("letter_l",r"C:\Users\Dell\Downloads")