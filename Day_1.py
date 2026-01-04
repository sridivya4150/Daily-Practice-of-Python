#writing a statement to print
print("Hello,World!")
#checking python version 
import sys
print(sys.version)
#taking input from the users
name=input("enter your name:")
#taking multiple inputs in single line
g,b=input("enter your count:").split()
#saying hello to user
print("hello, ",name)
print("the no.of girls in the class:",g)
print("the no.of boys in the class :",b)
#giving multiple statements in single line(optional)
print('Hello, My Name is Sridivya ');print("I am currently learnig Python")
#variables
#declaring single variables
a=5;
print("declared variable is:",a)
#printing type of variable
print('type:',type(a))
#declaring multiple variables which having the same value
x=y=z=100
#declaring multiple variables which having different values
x1,x2,x3=20,30,40
print(x)
print(y)
print(z)
print(x1)
print(x2)
print(x3)
#keywords
#getting list of keywords
import keyword
print("the list of the keywords are:")
print(keyword.kwlist)

