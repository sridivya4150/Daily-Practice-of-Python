#python loops-while,for
#while-it execute a set of statements as long as a condition is true
i=1
while i>5:
    print(i)
    i+=1
#if we dont increment i or else the loop will continue forever
#break statement-by using break statement we can stop the loop even if the while condition is true
i=0
a="i love learning python"
while i<len(a):
    if a[i]=='e' or a[i]=='s':
        i +=1
        break
    print(a[i])
    i +=1
#continue statement--by using continue statement we can stop the current iteration,and continue with the next
i=0
while i<6:
    i += 1
    if i==3:
        continue
    print(i)
#while loop with else--it is executed only when the loop finishes normally
#if the loop is terminated using a break statement,the else block does not execute
a=0 
while a<5:
    a+=1
    print(a)
else:
    print("loop ended naturally")
while a<6:
    a +=1
    print(a)
    break
else:
    print("loop not ended naturally")
#challenge
i=1
print("-challenge start-")
while i<6:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1
else:
    print("Loop finished!")
#for loop-- it is used for iterating over a sequence 
#loop through string
for j in "apples":
    print(j)
#the break statement--the statement we can stop the loop before it has looped through all the items
fruits=[1,2,3,4,5]
for i in fruits:
    print(i)
    if i==4:
        break
print("loop ended")
for j in fruits:
    if j==3:
        break
    print(j)
#continue statement--we can stop the current iteration of the loop,and continue with the next
for k in fruits:
    if k==3:
        continue
    print(k)
#range() function
#to loop through a set of code a specified number of times, we can use the range().
#starting from 0 by default, and increments by 1 (by default),and ends at a specified number
for x in range(6):
    print(x)
#specifying the starting value by adding a parameter
for x in range(2,6):
    print(x)
#default increment the sequence by 1, specify the increment value by adding a third parameter
for x in range(2,30,3):
    print(x)
print("decrement")
#specifing decrement- by using -
for x in range(30,2,-3):
    print(x)


      



