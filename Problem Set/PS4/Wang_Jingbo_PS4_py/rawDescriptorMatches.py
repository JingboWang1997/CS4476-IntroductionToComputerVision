import scipy.io
import matplotlib.pyplot as plt
import numpy as np

from selectRegion import roipoly
from displaySIFTPatches import displaySIFTPatches
from dist2 import dist2

def rawDescriptorMatches(threshold):
    # keys:
    # ['__version__', '__header__', '__globals__', 'im1', 'descriptors2', 'im2', 'scales1', 'scales2', 'positions2',
    # 'descriptors1', 'positions1', 'orients2', 'orients1']
    mat = scipy.io.loadmat("twoFrameData.mat")
    im1 = mat['im1']
    im2 = mat['im2']

    # user select descriptors
    plt.imshow(im1)
    MyROI = roipoly(roicolor='r')
    Ind = MyROI.getIdx(im1, mat['positions1'])
    selectedDescriptors = mat['descriptors1'][Ind]

    # all image2 descriptors
    im2Descriptors = mat['descriptors2']

    # distance matrix
    # entry = dist2(x,c)
    # entry[i][j] corresponds to the distance between x[i] and c[j]
    dist = dist2(selectedDescriptors, im2Descriptors)

    # locate the distances that are less than threshold, and output the column as the index for descriptor2
    # set used for removing duplicates
    matchedIndices = list(set(np.where(dist < threshold)[1]))

    # display boxes
    fig = plt.figure()
    bx = fig.add_subplot(111)
    bx.imshow(im2)
    coners = displaySIFTPatches(mat['positions2'][matchedIndices, :], mat['scales2'][matchedIndices, :], mat['orients2'][matchedIndices, :])

    for j in range(len(coners)):
        bx.plot([coners[j][0][1], coners[j][1][1]], [coners[j][0][0], coners[j][1][0]], color='g', linestyle='-',
                linewidth=1)
        bx.plot([coners[j][1][1], coners[j][2][1]], [coners[j][1][0], coners[j][2][0]], color='g', linestyle='-',
                linewidth=1)
        bx.plot([coners[j][2][1], coners[j][3][1]], [coners[j][2][0], coners[j][3][0]], color='g', linestyle='-',
                linewidth=1)
        bx.plot([coners[j][3][1], coners[j][0][1]], [coners[j][3][0], coners[j][0][0]], color='g', linestyle='-',
                linewidth=1)
    bx.set_xlim(0, im2.shape[1])
    bx.set_ylim(0, im2.shape[0])
    plt.gca().invert_yaxis()
    plt.show()


rawDescriptorMatches(0.18)