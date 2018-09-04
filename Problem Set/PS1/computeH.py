import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# that takes a set of corresponding image points t1, t2 (both t1
# and t2 should be 2xN matrices) and returns the associated 3 x 3 homography matrix H. The function
# should take a list of n >= 4 pairs of corresponding points from the two views, where each point is
# specified with its 2d image coordinates.
def computeH(t1, t2):
    # scale down to [0, 2]
    # maximum = max(t1.max(), t2.max())
    # t1 = (t1/maximum) * 2
    # t2 = (t2/maximum) * 2

    # t1 = p, t2 = p'
    # make L matrix with all zeros for now
    L = np.zeros((t1.shape[1]*2, 9))
    # fill in the L matrix
    for i in range(t1.shape[1]):
        p = np.array([t1[0][i], t1[1][i], 1])
        zeros = np.zeros(3,)
        xprime = (-t2[0][i]) * p
        row1 = np.concatenate((p, zeros, xprime))
        yprime = (-t2[1][i]) * p
        row2 = np.concatenate((zeros, p, yprime))
        L[i*2] = row1
        L[(i*2) + 1] = row2
    # make A
    a = np.matmul(L.transpose(), L)
    print "a: ", a
    # find eigens, and find the eigenvector for the least eigenvalue
    eigens = np.linalg.eig(a)
    eigenvalues = eigens[0]
    eigenvectors = eigens[1]
    minindex = np.where(eigenvalues == eigenvalues.min())[0][0]
    solution = eigenvectors[:, minindex]
    H = solution.reshape((3, 3))
    return H/H[2, 2]


# points1 = np.load('./cc1.npy')
# points2 = np.load('./cc2.npy')
# H = computeH(points1.transpose(), points2.transpose())
#
# image1 = mpimg.imread("./crop1.jpg")
# image2 = mpimg.imread("./crop2.jpg")
# homo = np.concatenate((points1.transpose(), np.ones((1, 12))))
# transformed = np.matmul(H, homo)
# for i in range(transformed.shape[1]):
#     transformed[0, i] /= transformed[2, i]
#     transformed[1, i] /= transformed[2, i]
#     transformed[2, i] /= transformed[2, i]
# xaxis = transformed[0]
# yaxis = transformed[1]
# plt.imshow(image2)
# plt.plot(xaxis, yaxis, 'bo')
# plt.show()
