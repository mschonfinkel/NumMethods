def solve(A, b):
    n = len(A)
    x = [[0] for _ in range(n)]

    for k in range(n-1, -1, -1):
        s = sum(A[k][j]*x[j][0] for j in range(k+1, n))
        x[k][0] = (b[k][0] - s)/A[k][k]
    return x

def test():
    A = [[1, 2, 3],
         [0, 4, 5],
         [0, 0, 6]]

    b = [[1],
         [2],
         [3]]

    print(solve(A, b))

test()
