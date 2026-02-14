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



    





