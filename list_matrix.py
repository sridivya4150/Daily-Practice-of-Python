#matrix-- a matrix is a collection of numbers arranged in rows and columns
#python doesnot have built in matrix type
#matrix using list
matrix=[
    [1,2,3],
    [4,5,6]
]
#printing matrix
for row in matrix:
    print(row)
#Accessing matrix elements
#Accessing specific element
print(matrix[0][1])   # Row 0, Column 1 → 2
#Access full row
print(matrix[1])
#Access column elements
for row in matrix:
    print(row[0])     # First column elements
#taking matrix elements from  user
rows = int(input("rows: "))
col = int(input("columns: "))
matrix = [] 
print("entries row-wise:")
for i in range(rows):   
    row = []
    for j in range(col):
        row.append(int(input()))    # user input for rows
    matrix.append(row)  # adding rows to the matrix
print("\nyour matrix:")
for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()
#creating a matrix using list comprehension 
matrix = [[col for col in range(4)] for row in range(4)]
print(matrix)
#Assigning value in matrix-positive index,negative index
#by using positive index
matrix=[
    [1,2,3],
    [4,5,7]
]
matrix[1][1]=6
print(matrix)
#by using negative matrix
matrix=[-1][-1]=9
print(matrix)
#mathematical operations with matrix 
#Addition using loops
x = [[1,2,3],[4,5,6]]
y = [[4,6,7],[9,7,1]]

# initialize result matrix
res = [[0 for j in range(len(x[0]))] for i in range(len(x))]

# addition using loops
for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j] + y[i][j]

print("matrix addition:")
for r in res:
    print(r)

# addition using list comprehension
addition_res = [[x[i][j] + y[i][j] for j in range(len(x[0]))]
                                      for i in range(len(x))]
print("matrix addition:")
for row in addition_res:
    print(row)

# subtraction using loops
for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j] - y[i][j]

print("subtraction:")
for r in res:
    print(r)

# subtraction using list comprehension
subtraction_res = [[x[i][j] - y[i][j] for j in range(len(x[0]))]
                                         for i in range(len(x))]
print("subtraction:")
for row in subtraction_res:
    print(row)
