#patter printing
rows=int(input("enter no.of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    