import numpy as np
import copy
import math

def find_norm(u):
    res = 0
    for val in u:
        res = res + val*val
    return math.sqrt(res)

def sign(a):
    if a == 0 or a == 0.0 or a == -0.0:
        return 1
    return a/abs(a)

def householder_vector(u):
    norm = find_norm(u)
    u[0] = u[0] + norm*sign(u[0])
    return u

def find_beta(u):
    res = 0
    for val in u:
        res = res + val*val
    return res

def householder_transformation(A):
    m = len(A)
    n = len(A[0])

    for k in range(0, m-1):
        u = []
        for i in range(k,m):
            u.append(A[i][k])
        
        u = householder_vector(u)
        beta = 2/find_beta(u)
        
        b = []
        for i in range(k, m):
            t = []
            for j in range(k, n):
                t.append(A[i][j])
            b.append(t)

        u_t = np.matrix(u)
        u = u_t.transpose()
        u = np.matmul(u, u_t)
        u = beta*u
        u = np.matmul(u, b)
        b = b - u
        
        b = b.tolist()

        for i in range(len(b)):
            for j in range(len(b[0])):
                val = round(b[i][j], 4)
                if val == 0.0 or val == -0.0:
                    A[i+k][j+k] = 0

                else:
                    A[i+k][j+k] = val
        
    print(A)



if __name__ == '__main__':
    m = int(input("Enter the no of rows of matrix A: "))
    n = int(input("Enter the no of columns of matrix A: "))

    A = []
    for i in range(m):
        t = []
        for j in range(n):
            a = float(input())
            t.append(a)
        A.append(t)

    householder_transformation(A)