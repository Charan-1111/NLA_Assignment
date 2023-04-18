import numpy as np

if __name__ == '__main__':
    m = int(input("Enter the no of rows in the matrix A: "))
    n = int(input("Entre the no of columns in the matrix A: "))

    A = []
    for i in range(m):
        t = [float(j) for j in input().split()]
        A.append(t)
    A = np.array(A)
    