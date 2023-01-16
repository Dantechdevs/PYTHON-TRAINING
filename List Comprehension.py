#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

fruits = ["apple", "banana", "cherry", "kiwi", "mango","Salad","cabbage","cucumber"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist) 