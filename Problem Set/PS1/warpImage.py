import numpy as np
import scipy.misc as scimc
import computeH
import matplotlib.pyplot as plt

def warpImage1(inputIm, refIm, H):
    # inverse warping for warpIm
    HInverse = np.linalg.inv(H)
    newIm = np.zeros((refIm.shape))
    for i in range(newIm.shape[0]):
        for j in range(newIm.shape[1]):
            # i -> y value, j -> x value
            curCoord = np.array([[j, i, 1]]).transpose()
            originalCoord = np.matmul(HInverse, curCoord)
            x = originalCoord[0][0]/originalCoord[2][0]
            y = originalCoord[1][0]/originalCoord[2][0]
            xi = x.astype(int)
            xj = y.astype(int)
            a = x - xi
            b = y - xj
            if x > 0 and x < inputIm.shape[1] - 1 and y > 0 and y < inputIm.shape[0] - 1:
                rgb = ((1 - a) * (1 - b) * inputIm[xj][xi]) + (a * (1 - b) * inputIm[xj][xi + 1]) + (a * b * inputIm[xj + 1][xi + 1]) + ((1 - a) * b * inputIm[xj + 1][xi])
                newIm[i][j] = rgb
    warpIm = newIm/255

    # define how big to set the frame
    topleft = np.matmul(H, np.array([[0], [0], [1]]))
    topleft = topleft/topleft[2][0]
    topright = np.matmul(H, np.array([[inputIm.shape[1] - 1], [0], [1]]))
    topright = topright/topright[2][0]
    bottomleft = np.matmul(H, np.array([[0], [inputIm.shape[0] - 1], [1]]))
    bottomleft = bottomleft / bottomleft[2][0]
    bottomright = np.matmul(H, np.array([[inputIm.shape[1] - 1], [inputIm.shape[0] - 1], [1]]))
    bottomright = bottomright / bottomright[2][0]
    widthrange = np.array([min(topleft[0][0], topright[0][0], bottomleft[0][0], bottomright[0][0]), max(topleft[0][0], topright[0][0], bottomleft[0][0], bottomright[0][0])])
    heightrange = np.array([min(topleft[1][0], topright[1][0], bottomleft[1][0], bottomright[1][0]), max(topleft[1][0], topright[1][0], bottomleft[1][0], bottomright[1][0])])

    x_offset = abs(widthrange[0]).astype(int) + 1 if widthrange[0] < 0 else 0
    y_offset = abs(heightrange[0]).astype(int) + 1 if heightrange[0] < 0 else 0

    ref_x = refIm.shape[1] + x_offset
    ref_y = refIm.shape[0] + y_offset
    bigFrame = np.zeros((max((heightrange[1] + y_offset).astype(int), ref_y), max((widthrange[1] + x_offset).astype(int), ref_x), 3))

    # inverse warping for big frame
    for i in range(bigFrame.shape[0]):
        for j in range(bigFrame.shape[1]):
            # i -> y value, j -> x value
            curCoord = np.array([[j, i, 1]]).transpose()
            curCoord[0][0] -= x_offset
            curCoord[1][0] -= y_offset
            originalCoord = np.matmul(HInverse, curCoord)
            x = originalCoord[0][0]/originalCoord[2][0]
            y = originalCoord[1][0]/originalCoord[2][0]
            xi = x.astype(int)
            xj = y.astype(int)
            a = x - xi
            b = y - xj
            if x > 0 and x < inputIm.shape[1] - 1 and y > 0 and y < inputIm.shape[0] - 1:
                rgb = ((1 - a) * (1 - b) * inputIm[xj][xi]) + (a * (1 - b) * inputIm[xj][xi + 1]) + (a * b * inputIm[xj + 1][xi + 1]) + ((1 - a) * b * inputIm[xj + 1][xi])
                bigFrame[i][j] = rgb
    # overlay the second image
    for i in range(refIm.shape[0]):
        for j in range(refIm.shape[1]):
            bigFrame[i + y_offset][j + x_offset] = refIm[i][j]
    mergeIm = bigFrame / 255
    return (warpIm, mergeIm)

def warpImage(inputIm, refIm, H):
    print "new warp"
    # define how big to set the big frame to fit everything
    corners = np.array([[0, inputIm.shape[1] - 1, 0, inputIm.shape[1] - 1], [0, 0, inputIm.shape[0] - 1, inputIm.shape[0] - 1], [1, 1, 1, 1]])
    newCorners = np.matmul(H, corners)
    widthrange = np.array([min(newCorners[0]/newCorners[2]), max(newCorners[0]/newCorners[2])])
    heightrange = np.array([min(newCorners[1]/newCorners[2]), max(newCorners[1]/newCorners[2])])

    x_offset = abs(widthrange[0]).astype(int) + 1 if widthrange[0] < 0 else 0
    y_offset = abs(heightrange[0]).astype(int) + 1 if heightrange[0] < 0 else 0

    ref_x = refIm.shape[1] + x_offset
    ref_y = refIm.shape[0] + y_offset
    bigFrame = np.zeros(
        (max((heightrange[1] + y_offset).astype(int), ref_y), max((widthrange[1] + x_offset).astype(int), ref_x), 3))

    # inverse warping for big frame
    HInverse = np.linalg.inv(H)
    for i in range(bigFrame.shape[0]):
        for j in range(bigFrame.shape[1]):
            # i -> y value, j -> x value
            curCoord = np.array([[j, i, 1]]).transpose()
            curCoord[0][0] -= x_offset
            curCoord[1][0] -= y_offset
            originalCoord = np.matmul(HInverse, curCoord)
            x = originalCoord[0][0] / originalCoord[2][0]
            y = originalCoord[1][0] / originalCoord[2][0]
            xi = x.astype(int)
            xj = y.astype(int)
            a = x - xi
            b = y - xj
            if x > 0 and x < inputIm.shape[1] - 1 and y > 0 and y < inputIm.shape[0] - 1:
                rgb = ((1 - a) * (1 - b) * inputIm[xj][xi]) + (a * (1 - b) * inputIm[xj][xi + 1]) + (
                            a * b * inputIm[xj + 1][xi + 1]) + ((1 - a) * b * inputIm[xj + 1][xi])
                bigFrame[i][j] = rgb

    # crop bigFrame for warpIm
    newIm = np.zeros((refIm.shape))
    for i in range(newIm.shape[0]):
        for j in range(newIm.shape[1]):
            # i -> y value, j -> x value
            newIm[i][j] = bigFrame[i + y_offset][j + x_offset]
    warpIm = newIm/255

    # overlay the second image
    for i in range(refIm.shape[0]):
        for j in range(refIm.shape[1]):
            bigFrame[i + y_offset][j + x_offset] = refIm[i][j]
    mergeIm = bigFrame / 255
    return (warpIm, mergeIm)