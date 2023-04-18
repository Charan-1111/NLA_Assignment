import numpy as np
def givens_rotation(A):
    """
    QR-decomposition of rectangular matrix A using the Givens rotation method.
    """

    # Initialization of the orthogonal matrix Q and the upper triangular matrix R
    n, m = A.shape
    Q = np.eye(n)
    R = np.copy(A)

    rows, cols = np.tril_indices(n, -1, m)
    for (row, col) in zip(rows, cols):
        # If the subdiagonal element is nonzero, then compute the nonzero
        # components of the rotation matrix
        if R[row, col] != 0:
            r = np.sqrt(R[col, col]**2 + R[row, col]**2)
            c, s = R[col, col]/r, -R[row, col]/r

            # The rotation matrix is highly discharged, so it makes no sense
            # to calculate the total matrix product
            R[col], R[row] = R[col]*c + R[row]*(-s), R[col]*s + R[row]*c
            Q[:, col], Q[:, row] = Q[:, col]*c + Q[:, row]*(-s), Q[:, col]*s + Q[:, row]*c

    return Q[:, :n], R[:n]

if __name__ == '__main__':
    m = int(input("Enter the no of rows in the matrix A: "))
    n = int(input("Enter the no of columns in the matrix A: "))

    A = []
    for i in range(m):
        t = [float(j) for j in input().split()]
        A.append(t)
    A = np.array(A)

    np.set_printoptions(precision=4, suppress=True)
    # Print input matrix
    print('The A matrix is equal to:\n', A)
    # Compute QR decomposition using Givens rotation
    Q, R = givens_rotation(A)

    # Print orthogonal matrix Q
    print('\n The Q matrix is equal to:\n', Q)

    # Print upper triangular matrix R
    print('\n The R matrix is equal to:\n', R)

    print(Q@R)