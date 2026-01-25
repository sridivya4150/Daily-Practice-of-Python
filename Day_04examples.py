#this problems are sloved only using operators its not included any conditional statements are anything 
#Input a number and print:1.square 2.cube
a=int(input("enter your number:"))
print("square of",a,":",a**2)
print("cube of",a,":",a**3)
#Take two integers and print the remainder when first is divided by second
num1=int(input("enter your num1:"))
num2=int(input("enter your num2:"))
print("the remainder of", num1 ,"divided by", num2 ,"is :", num1%num2)
#Input a number and check whether it is even or odd using an operator only
num3=int(input("enter your value:"))
print("is it",num3," even?",num3%2==0)
print("is it",num3," odd?",num3%2!=0)
#Take two numbers and find the greater number using operators
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
print(b, "is greater" * (b > c), c, "is greater" * (c > b))
#or
print("greater value is:",max(b,c))
#Input age and check if the person is eligible to vote.
age=int(input("enter your age:"))
print('your eligible to vote'*(age>=18))
print('you are not eligible to vote'*(age<18))
#Take a number and check whether it lies between 10 and 50
number=int(input("enter a number:"))
print("is it",number,"lies between 10 to 50:",10>number>50)

