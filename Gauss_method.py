import numpy as np

from GF import GF


def gauss(A, b, F):
    A = np.append(A, b, axis=1)
    A = A.astype(int)
    n = len(A)

    for i in range(n):
        for k in range(n, -1, -1):
            A[i, k] = (F.mul([A[i][k]], F.inv([A[i][i]]))[:1] or [0])[0]

        for k in range(i + 1, n):
            for l in range(n, i - 1, -1):
                A[k, l] = (F.mul([A[k][l]], F.inv([A[k][i]]))[:1] or [0])[0]
                A[k, l] = (F.add([A[k, l]], [-A[i, l]])[:1] or [0])[0]

    for i in range(n - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            for l in range(n, -1, -1):
                mult = (F.mul([A[i, l]], [A[k, i]])[:1] or [0])[0]
                A[k, l] = (F.add([A[k, l]], [-mult])[:1] or [0])[0]
    return A[:, -1]
