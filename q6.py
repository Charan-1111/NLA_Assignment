import numpy as np

def SVD(A):
    ATA = np.dot(A.T, A)
    evals, V = np.linalg.eig(ATA)
    idx = np.argsort(evals)[::-1]
    evals = np.sqrt(evals[idx])
    V = V[:, idx]
    U = np.dot(A, V) / evals

    return U, np.diag(evals), V.T

if __name__ == '__main__':
    m = int(input("Enter the no of rows in the matrix A: "))
    n = int(input("Enter the no of columns in the matrix A: "))

    A = []
    for i in range(m):
        t = [float(j) for j in input().split()]
        A.append(t)

    A = np.array(A)

    U, S, VT = SVD(A)
    print(A)

    print(U)
    print(S)
    print(VT)
    print(U.dot(S.dot(VT)))