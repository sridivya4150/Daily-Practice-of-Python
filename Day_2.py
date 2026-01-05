#Data Types
#numeric--int,float,complex
#int
#taking integer as input
a=int(input("enter your number:"))
#type conversion-converting objects from one data type to anthor data type
#converting string to int
name='Python'
print(int(name))
#converting float to int
print("int(9.5):",int(9.5))
#octal to decimal using int()
print("int() on 12=",int('12',8))
#binary to decimal using int()
print("int() on 110:",int(110,2))
#float
#taking float as input
b=float(input("enter your float value:"))
#printing the float value
print("b=",b)
#printing float value with precision
print(f"b= {b:.2f}")
#complex
#creating complex numbers
c1=complex(4,6)#returns x+yj
c2=complex(5)#returns x+0j
c3=complex()#returns 0j
print(c1)
print(c2)
print(c3)
#complex with int and float parameters
c4=complex(3,4)#with integer
print(c4)
c5=comples(3.3,4.7)#with float
print(c5)
#complex with strings
c6=complex('4.6')
print(c6)
c7=complex("5.8","9.2")
print(c7)
#taking complex data type as input
c=complex(input("Enter a complex number:"))
print(c)
#method 2
r=float(input("Enter real part:"))
i=float(input("Enter imaginary part:"))
c8=complex(r,i)
print(c8)
#method3
r1, i1= map(float, input("Enter real and imaginary: ").split())
equa=complex(r1,i1)
print(r1, i1)
#random numbers
import random
print(random.randrange(1,10))
#sequence type:string,tuple,list
#mapping type:dict
#boolean type:bool
#set type:set,frozenset
#binary types:bytes,bytearraay,memoryview
#checking type of the variables
num1=5
num2=5.89
num3=4+6j
num4="python" 
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))








