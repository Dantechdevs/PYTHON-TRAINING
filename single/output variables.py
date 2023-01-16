#The Python print() function is often used to output variables
x = "Python is awesome"
print(x)

#multiple variables are separated by comma
x ="mangoes,orange ,banana,teacher,sex,"
print(x)

#You can also use the + operator to output multiple variables:

x ="2"
y ="4"
z ="3"
print(x+y+z)


#GLOBAL VARIABLES
x = "awesome"

def myfunc():
    print("Python is")
    myfunc()

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

    myfunc()

print("Python is " + x) 