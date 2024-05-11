#Assignment 1

def reverse_string (my_string) :
    yield my_string[-1:]

for c in reverse_string("majd") :
    print (c)

#Assignment 2 

def deco (func) :
    def nested_func ():
        print("Sugar Added From Decorators")
        func()
        print("####################")
    return nested_func

@deco
def make_tea():
    print("Tea Created")


@deco
def make_coffee():
    print("Coffe Created")

make_coffee()
make_tea()

