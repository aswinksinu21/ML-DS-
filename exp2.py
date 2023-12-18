import numpy as np
matrix = np.array([[5,6,6],[1,2,3],[7,8,3]])
u,s,vt = np.linalg.svd(matrix)
print(u)
print(np.diag(s))
print(vt)
rematrix = np.dot(u,np.dot(np.diag(s),vt))
print(rematrix)