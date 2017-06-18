# Adapted from Cormen

import numpy as np

def LU_dec(A):
    n = len(A)
    
    L = np.zeros((n,n))
    U = np.zeros((n,n))

    for i in range(n):
        L[i,i] = 1.0
        U[i,i] = 1.0

    for k in range(n):
        U[k,k] = A[k,k]
        for i in range(k+1,n):
            L[i,k] = A[i,k]/U[k,k]
            U[k,i] = A[k,i]

        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i,j] = A[i,j] - L[i,k]*U[k,j]

    return L, U

A = np.array(
    [[2, 3, 1, 5],
    [6, 13, 5, 19],
    [2, 19, 10, 23],
    [4, 10, 11, 31]]
)

L,U = LU_dec(A)

pprint = lambda m: '\t' + '\n\t\t'.join(' '.join('{:6s}'.format(str(y)) for y in line) for line in m) + '\n'

print("A = " + pprint(A))
print("L = " + pprint(L))
print("U = " + pprint(U))

