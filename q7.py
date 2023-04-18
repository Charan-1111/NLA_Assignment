import numpy as np
import copy
import math

def make_column_vector(A, k):
    n = len(A)
    u = []
    for i in range(0, n):
        u.append(A[i][k])
    return u

def find_norm(u):
    res = 0
    for val in u:
        res = res + val*val
    return round(math.sqrt(res),4)

def transform(A, k, norm):
    n = len(A)
    for i in range(n):
        A[i][k] = round(A[i][k]/norm, 4)

def find_product(A, k, j):
    n = len(A)
    ak = []
    aj = []

    for i in range(0, n):
        ak.append(A[i][k])
        aj.append(A[i][j])
    
    aj = np.matrix(aj)
    aj = aj.transpose()
    aj = np.matmul(ak, aj)
    aj = aj.tolist()
    return aj[0][0]

def make_transform(A, j, k, val):
    n =  len(A)
    
    for i in range(0, n):
        A[i][j] = A[i][j] - (val * A[i][k])

def QR_factorization_using_MGS(A):
    n = np.linalg.matrix_rank(A)

    R = np.zeros((n, n))

    for k in range(0, n):
        ak = make_column_vector(A, k)
        R[k][k] = find_norm(ak)

        transform(A, k, R[k][k])

        for j in range(k+1, n):
            R[k][j] = find_product(A, k, j)
            make_transform(A, j, k, R[k][j])

    return A, R

if __name__ == '__main__':
    n = int(input("Enter the dimension of the matrix A: "))
    A = []
    for i in range(n):
        t = [float(j) for j in input().split()]
        A.append(t)

    A = np.array(A)
    Q, R = QR_factorization_using_MGS(A)

    print("============ Orthogonal Matrix Q after transformation ============")
    print(Q)
    print("============ Upper Triangular Matrix R after transformation ============")
    print(R)