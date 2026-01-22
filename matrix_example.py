#taking matrices from users and performing operations on it
#matrix1
rows = int(input("rows: "))
col = int(input("columns: "))
matrix1 = [] 
print("entries row-wise:")
for i in range(rows):   
    row = []
    for j in range(col):
        row.append(int(input()))    # user input for rows
    matrix1.append(row)  # adding rows to the matrix
print("\nyour matrix:")
for i in range(rows):
    for j in range(col):
        print(matrix1[i][j], end=" ")
    print()
#matrix2
rows = int(input("rows: "))
col = int(input("columns: "))
matrix2 = [] 
print("entries row-wise:")
for i in range(rows):   
    row = []
    for j in range(col):
        row.append(int(input()))    # user input for rows
    matrix2.append(row)  # adding rows to the matrix
print("\nyour matrix:")
for i in range(rows):
    for j in range(col):
        print(matrix2[i][j], end=" ")
    print()
#addition
add_res=[[matrix1[i][j]+matrix2[i][j] for j in range(len(matrix1[0]))]
         for i in range(len(matrix1))]
print("addition of matrix:")
for row in add_res:
    print(row)
#subtraction
sub_res=[[matrix1[i][j]-matrix2[i][j] for j in range(len(matrix1[0]))]
         for i in range(len(matrix1))]
print("matrix subtraction:")
for row in sub_res:
    print(row)
#multiplication
mul_res=[[matrix1[i][j]*matrix2[i][j] for j in range(len(matrix1[0]))]
         for i in range(len(matrix1))]
print("matrix multiplication:")
for row in mul_res:
    print(row)
#division
div_res=[[matrix1[i][j]/matrix2[i][j] for j in range(len(matrix1[0]))]
         for i in range(len(matrix1))]
print("matrix division:")
for row in div_res:
    print(row)
#transpose
transpose=[[matrix1[i][j] for i in range(len(matrix1))]for j in range(len(matrix1[0]))]
print("matrix1 transpose:")
for row in transpose:
    print(row)