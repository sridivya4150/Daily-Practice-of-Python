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

