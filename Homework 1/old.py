def matrix(A,B):
    n = len(A)
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            #print(i,j)
            cij = 0
            for k in range(n):
                #thing = A[i][k] * B[k][j]
                acom = A[i][k]
                bcom = B[k][j]
                thing = acom*bcom
                #print(acom,bcom)
                cij += thing
            #print(cij)
            #print("cij " + str(c[i][j]))
            c[i][j] = cij
            print(c)
            print(c[j][i])

    return c

print(matrix([[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]))
