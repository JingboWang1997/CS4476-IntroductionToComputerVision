from skimage import feature
from skimage import color
import numpy as np
import math
from numpy import unravel_index
from scipy import ndimage

import matplotlib.pyplot as plt

def detectCircles(im, radius, useGradient):
    # get canny edge image
    grayImage = color.rgb2gray(im)
    cannyImage = feature.canny(grayImage)
    # centers can be out of the image, so append the sides
    accumulatorArrays = np.zeros((cannyImage.shape[0] + (2 * radius), cannyImage.shape[1] + (2 * radius)))

    if not useGradient:
        # iterate over the edge image
        for i in xrange(cannyImage.shape[0]): #row, y
            for j in xrange(cannyImage.shape[1]): #column, x
                # upper left corner is (0,0), (x,y)
                x = j
                y = i
                if cannyImage[i][j] == True:
                    for theta in xrange(360):
                        # accumulatorArrays (b + 2r) x (a + 2r)
                        a = int(round(radius + (x - (radius * math.cos(theta * (math.pi / 180))))))
                        b = int(round(radius + (y + (radius * math.sin(theta * (math.pi / 180))))))
                        accumulatorArrays[b][a] += 1
    else:
        # get gradient and thetas
        dy, dx = np.gradient(grayImage)
        arctanMatrix1 = np.arctan2(dy, dx)
        arctanMatrix2 = np.arctan2(-dy, dx)
        arctanMatrix3 = np.arctan2(dy, -dx)
        arctanMatrix4 = np.arctan2(-dy, -dx)

        for i in xrange(cannyImage.shape[0]):  # rows, y
            for j in xrange(cannyImage.shape[1]):  # columns, x
                # upper left corner is (0,0), (x,y)
                x = j
                y = i
                if cannyImage[i][j] == True:
                    # for theta in xrange(int(thetaMatrix[i][j]-90), int(thetaMatrix[i][j]+90)):
                        # accumulatorArrays b + 2r x a + 2r
                    theta1 = arctanMatrix1[i][j]
                    theta2 = arctanMatrix2[i][j]
                    theta3 = arctanMatrix3[i][j]
                    theta4 = arctanMatrix4[i][j]
                    a = int(round(radius + (x - (radius * math.cos(theta1)))))
                    b = int(round(radius + (y + (radius * math.sin(theta1)))))
                    if b >= 0 and b < accumulatorArrays.shape[0] and a >= 0 and a < accumulatorArrays.shape[1]:
                        accumulatorArrays[b][a] += 1
                    a = int(round(radius + (x - (radius * math.cos(theta2)))))
                    b = int(round(radius + (y + (radius * math.sin(theta2)))))
                    if b >= 0 and b < accumulatorArrays.shape[0] and a >= 0 and a < accumulatorArrays.shape[1]:
                        accumulatorArrays[b][a] += 1
                    a = int(round(radius + (x - (radius * math.cos(theta3)))))
                    b = int(round(radius + (y + (radius * math.sin(theta3)))))
                    if b >= 0 and b < accumulatorArrays.shape[0] and a >= 0 and a < accumulatorArrays.shape[1]:
                        accumulatorArrays[b][a] += 1
                    a = int(round(radius + (x - (radius * math.cos(theta4)))))
                    b = int(round(radius + (y + (radius * math.sin(theta4)))))
                    if b >= 0 and b < accumulatorArrays.shape[0] and a >= 0 and a < accumulatorArrays.shape[1]:
                        accumulatorArrays[b][a] += 1

    # limiting the vote in a bin
    binSize = 5
    threshold = 0.9
    y_axis = accumulatorArrays.shape[0] / binSize
    x_axis = accumulatorArrays.shape[1] / binSize
    maximum = accumulatorArrays.max()
    thresholdValue = threshold * maximum
    centers = []
    for y in xrange(y_axis):
        for x in xrange(x_axis):
            # scope for each bin
            scope = accumulatorArrays[y * binSize : (y * binSize) + binSize, x * binSize : (x * binSize) + binSize]
            winner = scope.max()
            if winner >= thresholdValue:
                # in format of (y, x) in the larger grid
                winnerCoord = unravel_index(scope.argmax(), scope.shape)
                # in format of (x, y) in the original size grid
                globalCoord = ((x * binSize) + winnerCoord[1] - radius, (y * binSize) + winnerCoord[0] - radius)
                centers.append(globalCoord)
    plt.imshow(accumulatorArrays)
    plt.show()
    return centers

    # sum up the values in a bin, if selected as center, put the coordinate as the center of bin
    # binSize = 5
    # threshold = 0.9
    # y_axis = accumulatorArrays.shape[0] / binSize
    # x_axis = accumulatorArrays.shape[1] / binSize
    # quantizedArrays = np.zeros((y_axis, x_axis))
    # centers = []
    # for y in xrange(y_axis):
    #     for x in xrange(x_axis):
    #         # scope for each bin
    #         scope = accumulatorArrays[y * binSize: (y * binSize) + binSize, x * binSize: (x * binSize) + binSize]
    #         quantizedArrays[y][x] = scope.sum()
    # maximum = quantizedArrays.max()
    # thresholdValue = threshold * maximum
    # for y in xrange(y_axis):
    #     for x in xrange(x_axis):
    #         if quantizedArrays[y][x] >= thresholdValue:
    #             globalX = (x * binSize) + (binSize/2) - radius
    #             globalY = (y * binSize) + (binSize/2) - radius
    #             centers.append((globalX, globalY))
    # plt.imshow(accumulatorArrays)
    # plt.show()
    # return centers



