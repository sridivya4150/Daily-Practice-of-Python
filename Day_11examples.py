#Print whether it is positive, negative, or zero
num=int(input("enter your number:"))
if num>0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number your entered is zero")
#Input an integer and check if it is even or odd
if num%2==0:
    print("the number is even number")
else:
    print("the number is odd number")
#Input two numbers and print the greater one.
a,b=map(int,input("enter your numbers:").split())
if a>b:
    print("a is bigger than b")
else:
    print("b is bigger than a")
#Input three numbers and find the largest using if-elif
a,b,c=map(int,input("enter  your three numbers:").split())
if a>=b and a>=c:
    print("a is bigger number")
elif b>=a and b>=c:
    print("b is bigger number")
else:
    print("c is greater number")
#Input a year and check if it is a leap year
year=int(input("enter a year:"))
if year%400==0 or (year%4==0 and year % 100!=0):
    print("leap year")
else:
    print("not a leap year")
#Input a character and check if it is uppercase or lowercase
character=input("enter your character:")
if len(character)>1:
    print("please enter only one character")
elif character.isupper():
    print("character is uppercase")
else:
    print("character is lowercase")
#Electricity Bill
unit=int(input("enter your units:"))
if unit<=100:
    print("bill:",unit*1)
elif unit>101 and unit<200:
    print("bill:",unit*2)
else:
    print("bill:",unit*3)
#Salary Bonus
salary=int(input("enter your salary:"))
experience=int(input("enter your no.of years experience:"))
if experience>=5:
    print("bonus:",salary*(5/100))
#Character Type
char=input("enter your character:")
if len(char)>1:
    print("please enter only one character")
elif char.isalpha():
    print("the given character is alphabet")
elif char.isdigit():
    print("the given character is digit")
else:
    print("the given character is special character")
#Login System
username="admin"
password="1234"
in_username=input("enter username:")
in_password=input("enter password:")
if in_username==username and in_password==password:
    print("WELCOME")
else:
    print("error!,information is not matched")
#Calculator using if-elif
a,b=map(float,input("enter two integers:").split())
operator=input("enter operator(+,-,*,/):")
if operator=="+":
    print("addition:",a+b)
elif operator=="-":
    print("subtraction:",a-b)
elif operator=="/":
    print("division:",a/b)
elif operator=="*":
    print("multiplication:",a*b)
