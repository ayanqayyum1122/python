#string data type
import math
#litreal assignment
first = "ayan"
last = "qayyum"

# print(type(burger))
# print(type(burger) == str )           
# print(isinstance(first,str))

# contructor function
# burger = str("ham")
# print(type(burger))
# print(type(burger) == str )           
# print(isinstance(first,str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(2010)
print(type(decade))
print(decade)

statement = "i love python from the " + decade + "s."
print(statement)

# multiple lines 
multiline = ''' 
hey how are you ?                    

i was just chcking in.        
                               all good?'''
print(multiline) 

# escaping special characters
sentence = 'I\'m' 'running codes on visual studio!'' help!\n\n\where\'s this at\\located?'
print(sentence)

# string methods 

print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                               "
multiline = "                      " + multiline 
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("cake".ljust(16, ".") + "$100000000000".rjust(4))
print("cheesecake".ljust(16, ".") + "$16000".rjust(4))
print("mocha".ljust(16, ".") + "$1500".rjust(4))

print("")

# string index values
print(first[+1])
print(first[+1])
print(first[+1])

# some methods return boolean data
print(first.startswith("a"))
print(first.endswith("n"))

# boolean data type
myvalue = True
x = bool(False)
(type(x))
print(isinstance(myvalue, bool))

# numeric data type 

# integer type
price = 1000000
best_price = int(59)
print(type(price))
print((best_price, int))
 
# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa,1))

print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#  casting a string to number
zipcode = "100001"
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt to cast incorrect data
zip_value = int("lahore")





