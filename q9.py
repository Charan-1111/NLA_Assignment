import numpy as np
import copy
import math

def find_max(A):
    maxval = -1000
    for i in A:
        for j in i:
            maxval = max(maxval, abs(j))
    return maxval

def LU_transformation_using_GEPP(A, b):
    n = len(A)
    
    max_a = find_max(A)
    maxval = copy.deepcopy(max_a)

    for k in range(n-1):
        # Finding the pivoting row
        row = -1
        max_row_val = -1000
        for i in range(k, n):
            if A[i][k] > max_row_val:
                row = i
                max_row_val = A[i][k]

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
        maxval = max(maxval, find_max(A))

    growth_factor = maxval/max_a
    return growth_factor

if __name__ == '__main__':
    n = int(input("Enter the dimension of the matrix A: "))
    A = []
    for i in range(n):
        t = [float(j) for j in input().split()]
        A.append(t)
    
    b = []
    for i in range(n):
        b.append([float(input())])
    
    growth_factor = LU_transformation_using_GEPP(A,b)
    print("Growth Factor = {}".format(growth_factor))