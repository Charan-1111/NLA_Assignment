import numpy as np

def QR_factorization_using_Householder(A):
    m, n = A.shape
    Q = np.eye(m)

    R = A.copy()

    for k in range(m-1):
        x = R[k:, k]
        e = np.zeros_like(x)
        e[0] = np.sign(x[0])
        u = x + e*np.linalg.norm(x)
        u = u / np.linalg.norm(u)

        R[k:, k:] = R[k:, k:] - 2*np.outer(u, np.dot(u, R[k:, k:]))
        Q[k:, :] = Q[k:, :] - 2*np.outer(u, np.dot(u, Q[k:, :]))

    return Q.T, R

if __name__ == '__main__':
    m = int(input("Enter the no of rows for the matrix A: "))
    n = int(input("Enter the no of columns of the matrix A: "))

    A = []
    for i in range(m):
        t = [float(j) for j in input().split()]
        A.append(t)
    A = np.array(A)
    Q, R = QR_factorization_using_Householder(A)
    print(A)
    print("===== Q after factorization =====")
    print(Q)
    print('===== R after factorization =====')
    print(R)

    # basis of the null space of the given matrix is
    print(Q[:, -1])