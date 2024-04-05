#Assignment 1
my_List=[1,5,4,3,3,2,1]
#Sunique_list=


#Assignment 2
nums={1,2,3}
letters={"A","B","C"}
print(nums|letters)
print(nums.union(letters))
print(nums.symmetric_difference(letters))

#Assignment 3
my_set={1,2,3}
letters={"A","B","C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("B")
my_set.add("A")
print(my_set)
print(my_set.discard("C"))
#Assignment 4
set_one={1,2,3}
set_two={1,2,3,4,5,6}
print(set_one.issubset(set_two))
#Assignment 5
my_dict={"lang1":{"name":"HTML",
                  "progress":"90%"}
         ,"lang2":{"name":"CSS",
                   "progress":"80%"}
         ,"lang3":{"name":"Python",
                  "progress":"30%"}}
print("{} progress is {}".format(my_dict["lang1"]["name"],my_dict["lang1"]["progress"]))
print("{} progress is {}".format(my_dict["lang2"]["name"],my_dict["lang2"]["progress"]))
print("{} progress is {}".format(my_dict["lang3"]["name"],my_dict["lang3"]["progress"]))
my_dict.update({"lang4":{"name":"AI"
                         ,"progress":"20%"}})
print("{} progress is {}".format(my_dict["lang4"]["name"],my_dict["lang4"]["progress"]))


