import numpy as np
import copy
import math

def find_norm(u):
    res = 0
    for val in u:
        res = res + (val*val)

    return round(math.sqrt(res),4)

def sign(a):
    if a==0:
        return 1
    return a/abs(a)

def householder_vector(u):
    norm = find_norm(u)
    # print(norm)
    u[0] = u[0] + (norm*sign(u[0]))
    return u
    
def find_beta(u):
    res = 0
    for val in u:
        res = res + val*val
    return res

def householder_transformation(A):
    n = len(A)

    for k in range(0, n-1):
        u = []
        for i in range(k, n):
            u.append(A[i][k])

        b = []
        for i in range(k, n):
            t = []
            for j in range(k, n):
                t.append(A[i][j])
            b.append(t)


        u = householder_vector(u)
        # print(u)

        beta = 2/find_beta(u)
        u_t =  np.asmatrix(u)
        u = u_t.transpose()

        t = np.matmul(u, u_t)
        t = np.matmul(t, b)
        t = beta*t

        print(t)
        

if __name__ == "__main__":
    n = int(input("Enter the dimension of matrix A: "))

    A = []
    for i in range(0,n):
        t = [int(j) for j in input().split()]
        A.append(t)

    # print(A)

    householder_transformation(A)
