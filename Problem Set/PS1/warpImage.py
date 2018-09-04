import numpy as np
import scipy.misc as scimc
import computeH
import cv2
import matplotlib.pyplot as plt

def warpImage(inputIm, refIm, H):
    # inverse warping
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

    # plt.imshow(warpIm)
    # plt.show()

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
    print "topleft: ", topleft
    print "topright: ", topright
    print "bottomleft: ", bottomleft
    print "bottomright: ", bottomright
    print "widthrange: ", widthrange
    print "heightrange: ", heightrange
    x_offset = abs(widthrange[0]).astype(int) + 1 if widthrange[0] < 0 else 0
    y_offset = abs(heightrange[0]).astype(int) + 1 if heightrange[0] < 0 else 0
    print "x offset: ", x_offset
    print "y offset: ", y_offset
    bigFrame = np.zeros(((heightrange[1] + y_offset).astype(int), (widthrange[1] + x_offset).astype(int), 3))
    print "big frame: ", bigFrame.shape
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
    for i in range(ref.shape[0]):
        for j in range(ref.shape[1]):
            bigFrame[i + y_offset][j + x_offset] = ref[i][j]
    bigFrame /= 255
    plt.imshow(bigFrame)
    plt.show()


input = scimc.imread('./crop1.jpg')
print "input: ", input.shape
ref = scimc.imread('./crop2.jpg')
print "ref: ", ref.shape
t1 = np.load('./cc1.npy').transpose()
t2 = np.load('./cc2.npy').transpose()
H = computeH.computeH(t1, t2)
print "H: ", H

# im1Reg = cv2.warpPerspective(input, H, (ref.shape[1], ref.shape[0]))
# plt.imshow(im1Reg)
# plt.show()

warped = warpImage(input, ref, H)
plt.imshow(warped)
plt.show()