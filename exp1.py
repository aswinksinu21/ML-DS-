import numpy as np
rows1 = int(input("Enter the number of rows for matrix 1: "))
cols1 = int(input("Enter the number of columns for matrix 1: "))
matrix1=np.empty((rows1,cols1), dtype=float)
print("Enter the value of the first matrix:")
for i in range(rows1):
 for j in range(cols1):
  matrix1[i][j]=float(input(f"Enter element at position ({i + 1}, {j + 1}): "))
rows2 = int(input("Enter the number of rows for matrix 2: "))
cols2 = int(input("Enter the number of columns for matrix 2: "))
matrix2=np.empty((rows2,cols2), dtype=float)
print("Enter the value of the second matrix:")
for i in range(rows2):
 for j in range(cols2):
  matrix2[i][j]=float(input(f"Enter element at position ({i + 1}, {j + 1}): "))
print("\nMatrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
sum=np.add(matrix1,matrix2)
print("sum:", sum)
prod=np.multiply(matrix1,matrix2)
print("product:", prod)
sub=np.subtract(matrix1,matrix2)
print("subtract:", sub)
trp1=np.transpose(matrix1)
trp2=np.transpose(matrix2)
print("transpose:", trp1)
print("transpose:", trp2)