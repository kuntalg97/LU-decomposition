import numpy as np

#A = [[1.0,-3.0,2.0],[3.0,-1.0,3.0],[2.0,-3.0,1.0]]
A = [[1.0,3.0,2.0],[-3.0,-1.0,-3.0],[2.0,3.0,1.0]] # Each sub-list represents a row of the matrix

print ("A = ",A)

L = []
U = []
n = 3

L = [[0.0 for x in range(n)] for y in range(n)]
U = [[0.0 for x in range(n)] for y in range(n)]

for i in range (n):
    L[i][i] = 1.0        

# LU factorisation
for i in range (1,n+1):
    for k in range (1,i+1):
        dsum = 0.0        
        for j in range (1,k):            
            dsum += L[k-1][j-1]*U[j-1][i-1]            
        U[k-1][i-1] = A[k-1][i-1]-dsum        
    for k in range (i+1,n+1):
        dsum = 0.0
        for j in range (1,i):
            dsum += L[k-1][j-1]*U[j-1][i-1]
        L[k-1][i-1] = (A[k-1][i-1]-dsum)/U[i-1][i-1]

print (A)
print (L)
print (U)

LU = np.dot(L,U)
print (LU)

det_l = 1.0
det_u = 1.0
for i in range (1,n+1):
    det_l *= L[i-1][i-1]
    det_u *= U[i-1][i-1]

print ("The determinant of A matrix = ",det_l*det_u)    
