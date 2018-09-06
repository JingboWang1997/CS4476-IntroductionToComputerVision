import numpy as np

# t1, t2 are 2xN matrices
# t1 = p, t2 = p' (t2 = H x t1)
def computeH(t1, t2):
    print "computing homography matrix"
    # construct L matrix
    L = np.zeros((t1.shape[1]*2, 9))
    for i in range(t1.shape[1]):
        p = np.array([t1[0][i], t1[1][i], 1])
        zeros = np.zeros(3,)
        xprime = (-t2[0][i]) * p
        row1 = np.concatenate((p, zeros, xprime))
        yprime = (-t2[1][i]) * p
        row2 = np.concatenate((zeros, p, yprime))
        L[i*2] = row1
        L[(i*2) + 1] = row2
    # construct A
    a = np.matmul(L.transpose(), L)
    # find eigens, and find the eigenvector for the least eigenvalue
    eigens = np.linalg.eig(a)
    eigenvalues = eigens[0]
    eigenvectors = eigens[1]
    minindex = np.where(eigenvalues == eigenvalues.min())[0][0]
    solution = eigenvectors[:, minindex]
    # reformat for H
    H = solution.reshape((3, 3))
    return H/H[2, 2]
