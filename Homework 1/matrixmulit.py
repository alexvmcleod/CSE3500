def matrix(A,B):
    n = len(A)
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += A[i][k]*B[k][j] # <=== 2 operations
    return c