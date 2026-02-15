#Print Numbers from 1 to 10
for i in range(1,21):
    print(i)
#Print Even Numbers from 1 to 20
print("printing even number from 1-20")
for i in range(1,21):
    if i%2==0:
        print(i)
#Print Table of a Number
multipler=int(input("enter which number table you want:"))
for i in range(1,11):
    print(multipler,"x",i,"=",multipler*i)
#Sum of First N Natural Numbers
sum=int(input("enter a number:"))
print("the sum of ",sum,"natural numbers is:")
count=0
i=0
while i<=sum:
    count=count+i
    i+=1
print(count)
#Factorial of a Number
print("the factorial of",sum,"is :")
i=1
fact=1
while i<=sum:
    fact=fact*i
    i+=1
print(fact)
#Reverse a Number(using while loop)
number=1234
result=0
while number>0:
    remainder=number%10
    result=result*10+remainder
    number=number//10
print(result)
#Count Digits in a Number
input=56789
count=0
while input>0:
    count+=1
    input=input//10
print("the number of digits is:",count)
#Check Palindrome Number
num=input("enter your number:")
reverse=" "
for i in reverse:
    reverse=i+reverse
if reverse==num:
    print("the input you given is palindrome")
else:
    print("the input you given is not a palindrome")
#Prime Number Check
number=int(input("enter a number:"))
if number<=1:
    print("not a prime")
else:
    for i in range(2,number):
        if number%i==0:
            print("not a prime")
            break
    else:
        print('prime')
#Fibonacci Series (First 10 terms)
a=0
b=1
for i in range(10):
    print(a,end='')
    a,b=b,a+b

    





