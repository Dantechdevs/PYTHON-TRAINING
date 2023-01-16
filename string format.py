#In python we can combine numbers to strings
#We can combine numbers and strings using format () method
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {}

age = 30 
txt = "My Name is Daniel,and i'm {} "
print(txt.format(age))

#the format()takes different arguments
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))