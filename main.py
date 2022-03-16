# Beginner Python code

# = Is a comment that isnt used in the code and is ignored by the application manager can be used to describe or keep notes next to certain bits of code

# https://www.google.com/search?q=docstring+python&rlz=1C1GCEA_enGB995GB995&oq=docstr&aqs=chrome.2.69i57j0i512l6j69i60.3440j0j7&sourceid=chrome&ie=UTF-8

# https://www.programiz.com/python-programming/

# Variables example
# Variables are assigned to data (like x for example) so that changes can be implemented into the code and it can be used in 


X = 10
Y = "Coding"

print(X)
print(Y)

# ^Variables example ^ 
# Variables are assigned to data (like x for example) so that changes can be implemented into the code and it can be used in 

# Integers, Strings and Floats
X =  str(10)
Y =  int("3")
Z =  float(3)

print(X)
print(Y)
print(Z)

# Integers: In Python, integers are zero, positive or negative whole numbers without a fractional part and having unlimited precision, e.g. 0, 100, -10. The followings are valid integer literals in Python.

# String: is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation. Python has a built-in string class named str . Python strings are "immutable" which means they cannot be changed after they are created

# Floats: is used to represent real numbers and is written with a decimal point dividing the integer and fractional parts. For example, 97.98, 32.3+e18, -32.54e100 all are floating point numbers.

# Variables Cont.
# *Variables are case sensitive*

A = "Coding"
a = "Code"

print(a)
print(A)

# Single and Double Quotes
# String Variables can be declared by either using a single or a double quote

# Data Types
# There are many different types of built in data types they are important to get the data types
# Some data types are:
#    str = Text
#    Int, Float = Numeric
#    List, Tuple, Range = Sequence
#    Bool = boolean types 

# Getting Data Types
# getting a data type can be found when using the type() Function

B = 5
print(type(B))

# As this is an integer the console should reflect the <Class 'int'>
# This is the same as bool, str and float

# *Numbers*
# there are 2 different types of numbers in python with one being 'int' (Integer) and the other being a 'Float' 

# Integer * Must be a Whole number and can either be a positive or a negative number it cannot have any decimals
X = 1
print(type(X))

# Float * Can be either be a positive or a negative number and it must have decimals included
Y = 5.555
print(type(Y))

# Strings * Strings in python have to be surrounded by either single '' or double quotations ""
# When a string is in a single form like 'Hello world' or "Hello World" It does not matter weather or not it is in a double quotations or single both give the same output

print("Hello World")
print('Hello World')









# Multi-line Strings
# Multiline Strings can be attached to a variable with three quotes """ or with ''' 
# https://www.w3schools.com/python/gloss_python_multi_line_strings.asp

print("hello")






# Accessing strings and strings cont.
# python doesnt actually have a set data length exept a character with the length of 1
# strings can be accessed while in a veriable by using []

A = ("Hello world")

print (A[1])

# the reason this happens is because e is the 2nd letter in hello world, this happens as when a string is created like the one above "0" is the first letter so that would be H 

# H = 0
print (A[0])
# E = 1
print (A[1])
# l = 2
print (A[2])
# l = 3
print (A[3])
# o = 4
print (A[4])


#Finding the length of a string.

Z = ("Hello world$!")

print (len(Z))
# the answer of 13 characters should show up in the console as it knows how many letters otherwise known as characters in the "Z" variable



#Booleans
#Evaluating an expression with python
#Evaluating a expression through python will only get your a "True" or "False" answer

print 