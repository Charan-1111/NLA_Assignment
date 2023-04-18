import numpy as np

def eigenvalues(A):
    n = len(A)
    I = np.eye(n)
    eig_vals = np.zeros(n)
    for i in range(n):
        x = np.random.rand(n)
        x = x / np.linalg.norm(x)
        for j in range(30):
            x = A.dot(x)
            x = x / np.linalg.norm(x)
        eig_vals[i] = x.dot(A.dot(x))
        A = A - (eig_vals[i]*np.outer(x,x))
    return eig_vals

if __name__ == '__main__':
    m = int(input("Enter the no of rows in the matrix A: "))
    n = int(input("Enter the no of columns in the matrix A: "))

    A = []
    for i in range(m):
        t = [float(j) for j in input().split()]
        A.append(t)
    A = np.array(A)

    A_eigenvalues = eigenvalues(A)
    print("===== Eigenvalues of A =====")
    for i in range(len(A_eigenvalues)):
        print("X{}:".format(i+1), A_eigenvalues[i])

    E = np.dot(10**-4, A)
    E_eigenvalues = eigenvalues(E)
    print("===== Eigenvalues of E =====")
    for i in range(len(E_eigenvalues)):
        print("X{}:".format(i+1), E_eigenvalues[i])