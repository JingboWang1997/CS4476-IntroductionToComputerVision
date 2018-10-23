from skimage import feature
from skimage import color
import numpy as np
import math
from scipy import ndimage

import matplotlib.pyplot as plt

def detectCircles(im, radius, useGradient):
    grayImage = color.rgb2gray(im)
    cannyImage = feature.canny(grayImage)
    threshold = 0.9
    # centers can be out of the image
    accumulatorArrays = np.zeros((cannyImage.shape[0] + (2 * radius), cannyImage.shape[1] + (2 * radius)))

    if not useGradient:
        for i in xrange(cannyImage.shape[0]): #row, y
            for j in xrange(cannyImage.shape[1]): #column, x
                # upper left corner is (0,0)
                x = j
                y = i
                if cannyImage[i][j] == True:
                    for theta in xrange(360):
                        # accumulatorArrays b + 2r x a + 2r
                        a = int(round(radius + (x - (radius * math.cos(theta * (math.pi / 180))))))
                        b = int(round(radius + (y + (radius * math.sin(theta * (math.pi / 180))))))
                        accumulatorArrays[b][a] += 1
    else:
        dy, dx = np.gradient(grayImage)
        arctanMatrix = np.arctan2(dy, dx)
        thetaMatrix = arctanMatrix

        for i in xrange(cannyImage.shape[0]):  # rows, y
            for j in xrange(cannyImage.shape[1]):  # columns, x
                # upper left corner is (0,0)
                x = j
                y = i
                if cannyImage[i][j] == True:
                    # for theta in xrange(int(thetaMatrix[i][j]-90), int(thetaMatrix[i][j]+90)):
                        # accumulatorArrays b + 2r x a + 2r
                    theta = thetaMatrix[i][j]
                    a = int(round(radius + (x - (radius * math.cos(theta)))))
                    b = int(round(radius + (y + (radius * math.sin(theta)))))
                    if b >= 0 and b < accumulatorArrays.shape[0] and a >= 0 and a < accumulatorArrays.shape[1]:
                        accumulatorArrays[b][a] += 1
    maximum = accumulatorArrays.max()
    thresholdValue = threshold * maximum
    centers = np.argwhere(accumulatorArrays >= thresholdValue)
    centers[:, [1, 0]] = centers[:, [0, 1]]
    centers -= radius
    plt.imshow(accumulatorArrays)
    plt.show()
    return centers



