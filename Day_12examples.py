#patter printing
rows=int(input("enter no.of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()
    