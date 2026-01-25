#problems
#Take an integer and print its square
a=int(input("enter your number:"))
print("the square of the number is:",a**2)
#Take two integers and print their sum, difference, product.
num1=int(input("enter your number1:"))
num2=int(input("enter your numver2:"))
print("num1+num2=",num1+num2)#sum
print("num1-num2=",num1-num2)#difference
print("num1*num2=",num1*num2)#product
#Take a number of days and convert it into weeks and days
total_days=int(input("enter total no.of days:"))
weeks=total_days//7
days=total_days%7
print(f"{weeks} weeks {days}days")
#Take a 3-digit number and print the sum of its digits
n=int(input("enter a 3-digit number:"))
n=abs(n)
hundreds_digit=n//100
tens_digit=(n//10)%10
ones_digit=n%10
print("sum the digits in 3-digits number:",hundreds_digit+tens_digit+ones_digit)
#Take a float and print it with 2 decimal places.
num3=float(input("enter your number:"))
print(f"number:{num3:.2f}")
#average of two float numbers
num4=float(input("enter your number1:"))
num5=float(input("enter your number2:"))
average = (num4 + num5) / 2
print("average:", average)
#Take a float representing temperature in Celsius and convert it to Fahrenheit
celsius=float(input("Enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("temperature in fahrenheit:",fahrenheit)
#Take a float price and calculate 18% GST.
price=float(input("enter the price:"))
GST=(18/100)*price
print(GST)
#Take a float distance in km and convert it to meters.
distance=float(input("enter your distance in kilometers:"))
distance_meter=distance*1000
print(distance_meter,"meters")
#Take a complex number and print its real part & imaginary part
c=complex(input("enter a complex number:"))
c1=c.real
c2=c.imag
print(c1)
print(c2)
#Take real and imaginary parts separately and form a complex number.
real=float(input("enter real part:"))
imag=float(input("enter imaginary part:"))
equation=complex(real,imag)
print(equation)
#Take two complex numbers and print their sum.
comp1=complex(input("enter a complex number1:"))
comp2=complex(input("enter a complex number2"))
sum_comp=comp1+comp2
print(sum_comp)


