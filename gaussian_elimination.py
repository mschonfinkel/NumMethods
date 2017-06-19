import numpy as np

def solve(A, b):
    n = len(A)
    x = np.array([[0] for _ in range(n)], dtype=float)

    for k in range(n-1, -1, -1):
        s = sum(A[k,j]*x[j,0] for j in range(k+1, n))
        x[k,0] = (b[k] - s)/A[k,k]
    return x

def gaussian_elimination(A, b):
    A = np.append(A, b, axis=1)

    n = len(A)

    for i in range(0, n-1):
        max_elm_column = A[i,i]
        max_elm_line = i

        for index, el in enumerate(A[i:, i]):
            if abs(el) > max_elm_column:
                max_elm_column = el
                max_elm_line = index

        #print(A)

        if max_elm_column > A[i,i]:
            A[max_elm_line,:], A[i,:] = A[i,:], A[max_elm_line,:].copy()

        for j in range(i+1, n):
            c = A[j,i]/A[i,i]
            A[j,:] = A[j,:] - c*A[i,:]

    return A

A = np.array(
    [[1, 1, 1],
    [2, 1, 3],
    [3, 1, 6]], dtype=float)


b = np.array([[4],[7],[2]], dtype=float)

print(A)
print(b)

A_ = gaussian_elimination(A, b)

A, b = A_[:,range(len(A))], A_[:,-1]

print(solve(A, b))