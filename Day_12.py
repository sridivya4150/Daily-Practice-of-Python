#python loops-while,for,for each
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



