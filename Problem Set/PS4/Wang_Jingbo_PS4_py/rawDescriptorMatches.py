import scipy.io
import matplotlib.pyplot as plt
from selectRegion import roipoly
from displaySIFTPatches import displaySIFTPatches

def rawDescriptorMatches():
    # ['__version__', '__header__', '__globals__', 'im1', 'descriptors2', 'im2', 'scales1', 'scales2', 'positions2',
    # 'descriptors1', 'positions1', 'orients2', 'orients1']
    mat = scipy.io.loadmat("twoFrameData.mat")
    im1 = mat['im1']
    im2 = mat['im2']

    plt.imshow(im1)
    MyROI = roipoly(roicolor='r')
    Ind = MyROI.getIdx(im1, mat['positions1'])
    selectedDescriptors = mat['descriptors1'][Ind]
    im2Descriptors = mat['descriptors2']
    matchedIndices = []
    for im1descriptor in selectedDescriptors:
        bestDistance = float('inf')
        bestIndex = -1
        for index in range(len(im2Descriptors)):
            im2Descriptor = im2Descriptors[index]
            distance = getEuclideanDist(im1descriptor, im2Descriptor)
            if distance < bestDistance:
                bestDistance = distance
                bestIndex = index
        matchedIndices.append(bestIndex)

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

def getEuclideanDist(list1, list2):
    if len(list1) != len(list2):
        raise NameError("list dimension doesn't match")
    squaredDistance = 0
    for i in range(len(list1)):
        squaredDistance += (list1[i] - list2[i]) ** 2
    return squaredDistance ** 0.5


rawDescriptorMatches()