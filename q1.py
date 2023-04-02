import numpy as np
import copy

def LU_factorization_using_GEWP(A, b):
    n = len(A)
    for k in range(0, n-1):
        #forming the multipliers
        m = []
        for i in range(k+1, n):
            val = -1*(A[i][k]/A[k][k])
            m.append(val)

        for i in range(k+1,n):
            A[i][k] = 0
            b[i][0] = round(b[i][0] + (m[i-k-1]*b[k][0]), 4)
            for j in range(k+1, n):
                A[i][j] = round(A[i][j] + (m[i-k-1]*A[k][j]), 4)
    # print("===== through GEWP =====")
    # for i in A:
    #     for j in i:
    #         print(j, end=" ")
    #     print()

    # for i in b:
    #     print(i) 

def solve_using_GEWP(M, B):
    A = copy.deepcopy(M)
    b = copy.deepcopy(B)
    n = len(A)
    
    LU_factorization_using_GEWP(A,b)

    # Finding the inverse of the matrix A after transforming it
    # into Upper triangular matrix
    A1 = np.linalg.inv(A)

    # Finding the solution
    x = np.matmul(A1,b)

    for i in range(n):
        x[i][0] = round(x[i][0], 4)
    
    print("======== Solution using Gaussian Elimination without Pivoting ========") 
    for i in range(n):
        print('X{} : '.format(i+1), x[i][0])

    # t = np.matmul(M, x)
    # print(t)

def LU_factorization_using_GEPP(A,b):
    n = len(A)
    
    for k in range(0, n-1):
        # Finding the pivoting row
        row = -1
        maxval = -1000
        for i in range(k, n):
            if A[i][k] > maxval:
                row = i
                maxval = A[i][k]
        
        for j in range(k, n):
            A[k][j], A[row][j] = A[row][j], A[k][j]
        b[k], b[row] = b[row], b[k]


        # Forming the multipliers
        m = []
        for i in range(k+1, n):
            val = -1*(A[i][k]/A[k][k])
            m.append(val)
        
        for i in range(k+1, n):
            A[i][k] = 0
            b[i][0] = round(b[i][0]+(m[i-k-1]*b[k][0]), 4)
            for j in range(k+1, n):
                A[i][j] = round(A[i][j]+(m[i-k-1]*A[k][j]), 4)
    # print("===== through GEPP =====")
    # for i in A:
    #     for j in i:
    #         print(j, end=" ")
    #     print()

    # for i in b:
    #     print(i)

def solve_using_GEPP(M,B):
    A = copy.deepcopy(M)
    b = copy.deepcopy(B)
    n = len(A)

    LU_factorization_using_GEPP(A,b)

    # Finding the inverse of the matrix A after 
    # transforming it into Upper traiangular matrix
    A1 = np.linalg.inv(A)

    # Finding the solution
    x = np.matmul(A1, b)

    for i in range(n):
        x[i][0] = round(x[i][0], 4)


    print("======== Solution using Gaussian Elimination with Pivoting ========")
    for i in range(n):
        print('X{} : '.format(i+1), x[i][0])

    # t = np.matmul(M, x)
    # print(t)


if __name__ == '__main__':
    n = int(input("Enter the dimension of the matrix A: "))

    # Taking the input matix A
    M = []
    for i in range(0,n):
        t = [int(j) for j in input().split()]
        M.append(t)

    B = []
    for i in range(0,n):
        B.append([int(input())])

    solve_using_GEWP(M,B)
    solve_using_GEPP(M,B)