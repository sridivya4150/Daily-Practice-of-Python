#patter printing
rows=5
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("reverse pattern")
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#printing numbers pattern
for i in range(rows):
    for j in range(i):
        print(i,end=" ")
    print(" ")
#pyramid pattern in python
rows=5
for i in range(1,rows+1):
    for j in range(rows -i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()
