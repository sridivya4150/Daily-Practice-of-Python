#Boolean values -- True or False
#comparing two values to get boolean answer
print(10>5)
print(10==5)
print(10<5)
#boolean values with variables
a=25
b=6
print(a==b)
print(a<b)
print(a!=b)
print(a>b)
#boolean chaining
print(10>5 and 5>2)
#or
print(10>5>2)
#boolean arithmetics---True=1;False=0
print(True+True)
print(True+False)
print(False+False)
#boolean type
a=True
print(type(a))
print(bool(0))        # False
print(bool(""))       # False
print(bool(10))       # True
print(bool("Hi"))     # True
#operators-9 types
#Arithmetic Operator- +,-,*,/,//,**,%
#arithmetic operations  are used with numeric values to perform common mathematical operations
x=int(input("enter your num1="))
y=int(input("enter your num2="))
print("addition:",x+y)
print("subtraction:",x-y)
print("Multiplication:",x*y)
print("division:",x/y)
print("modulus:",x%y)
print("floor division:",x//y)
print("exponentiation:",x**y)
#Assignment operator- =,+=,-=,*=,/=,%=,//=,**=,&=,....
#Assignment operators are used to assign values to variables
x_1 = 10
print("x_1:",x_1)
x_1 += 3
print("x_1:",x_1)
x_1-= 5
print("x_1:",x_1)
x_1 /= 2
print("x_1:",x_1)
x_1 %= 3
print("x_1:",x_1)
#walrus operator
print(num := 3)
#comparison Operators-==,!=,>,<,>=,<=
x = int(input("enter value of x:"))
y = int(input("enter value of y:"))
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
#Logical Operators- and, or, not
x=5
print(x<5 and x<10)#returns True if both statements are true
print(x<5 or x<4)#returns True if one of the statements is true
print(x<5 and x<10)#reverse the result returns False if the result is true
#identity operator- is, is not
'''Identity operators are used to compare the objects, 
not if they are equal, but if they are actually the same 
object, with the same memory location'''
x_1= ["apple", "banana"]
y_1= ["apple", "banana"]
z = x
print(x is z)
print(x is y)#is - Checks if both variables point to the same object in memory
print(x == y)#== - Checks if the values of both variables are equal
#Membership Operators-- in ,not in
#Membership operators are used to test if a sequence is presented in an object
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)#returns True if a sequence with the specified value is present in the object
print("grapes" not in  fruits)#Returns True if a sequence with the specified value is not present in the object	x not in y	
#Bitwise operators--&,|,^,~,<<,>>
#Bitwise operators are used to compare (binary) numbers
print("3 & 4:",3&4)#AND-Sets each bit to 1 if both bits are 1
print("3|4:",3|4)#OR-Sets each bit to 1 if one of two bits is 1
print("3^4:",3^4)#XOR-Sets each bit to 1 if only one of two bits is 1
print("~3:",~3)#NOT-Inverts all the bits
print("3<<2:",3<<2)#Zero fill left shift-Shift left by pushing zeros in from the right and let the leftmost bits fall off
print("3>>2:",3>>2)#signed right shift-Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

 








