import numpy as np

print("MATRIX 1")
r1=int(input("Enter the number of rows:"))
c1=int(input("Enter the number of columns:"))
print("Enter the matrix elements :")
entry=list(map(int,input().split()))
mat1=np.array(entry).reshape(r1,c1)
print("\nMATRIX 1\n",mat1)

print("\nMATRIX 2")
r2=int(input("Enter the number of rows:"))
c2=int(input("Enter the number of columns:"))
print("Enter the matrix elements :")
entry=list(map(int,input().split()))
mat2=np.array(entry).reshape(r2,c2)
print("\nMATRIX 2\n",mat2)

# 1. Dot Product

print("\nDOT PRODUCT\n")
print(np.dot(mat1,mat2))

# 2. Transpose

print("\nTRANSPOSE\n",mat1.transpose())
print(mat2.transpose())

# 3. Trace

print("\nTRACE OF MATRIX 1:\n",np.trace(mat1))
print("\nTRACE OF MATRIX 2:\n",np.trace(mat2))

# 4. Rank

print("\nRANK OF MATRIX 1:\n",np.linalg.matrix_rank(mat1))
print("\nRANK OF MATRIX 2:\n",np.linalg.matrix_rank(mat2))

# 5. Determinant

print("\nDETRMINANT OF MATRIX 1:\n",np.linalg.det(mat1))
print("\nDETRMINANT OF MATRIX 2:\n",np.linalg.det(mat2))

# 6. Inverse

print("\nINVERSE OF MATRIX 1:\n",np.linalg.inv(mat1))
print("\nINVERSE OF MATRIX 2:\n",np.linalg.inv(mat2))

#7. Eigen values and Eigen vectors

a, b = np.linalg.eig(mat1)
x, y = np.linalg.eig(mat2)
print("\nEIGEN VALUES AND EIGEN VECTORS OF MATRIX 1:\n")
print("\neigen value:\n",a)
print("\neigen vectors:\n",b)
print("\nEIGEN VALUES AND EIGEN VECTORS OF MATRIX 2:\n")
print("\neigen value:\n",x)
print("\neigen vector:\n",y)