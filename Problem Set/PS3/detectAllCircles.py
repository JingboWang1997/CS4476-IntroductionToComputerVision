from skimage import feature
from skimage import color
import numpy as np
import math
from numpy import unravel_index
from scipy import ndimage
from progressBar import progress

import matplotlib.pyplot as plt

def detectAllCircles(im):
    # get canny edge image
    grayImage = color.rgb2gray(im)
    cannyImage = feature.canny(grayImage)
    # centers can be out of the image, so append the sides
    accumulatorArrays = np.zeros((cannyImage.shape[0], cannyImage.shape[1], min(im.shape[0], im.shape[1])/2))
    print accumulatorArrays.shape
    # iterate over the edge image
    for i in xrange(cannyImage.shape[0]): #row, y
        for j in xrange(cannyImage.shape[1]): #column, x
            # upper left corner is (0,0), (x,y)
            # progress((i * cannyImage.shape[1]) + j, cannyImage.shape[0] * cannyImage.shape[1], status="1")
            x = j
            y = i
            if cannyImage[i][j] == True:
                for theta in xrange(360):
                    for radius in xrange(accumulatorArrays.shape[2]):
                        progress(((i * cannyImage.shape[1] * 360 * accumulatorArrays.shape[2]) + (j * 360 * accumulatorArrays.shape[2]) + (theta * accumulatorArrays.shape[2]) + radius), cannyImage.shape[0] * cannyImage.shape[1] * 360 * accumulatorArrays.shape[2], status="1")
                        a = int(round(x - (radius * math.cos(theta * (math.pi / 180)))))
                        b = int(round(y + (radius * math.sin(theta * (math.pi / 180)))))
                        if a >= 0 and a < accumulatorArrays.shape[1] and b >= 0 and b < accumulatorArrays.shape[0] and radius >= 0 and radius < accumulatorArrays.shape[2]:
                            accumulatorArrays[b][a][radius] += 1

    # limiting the vote in a bin
    # binSize = 1
    lowerThreshold = 0.5
    upperThreshold = 0.8
    # y_axis = accumulatorArrays.shape[0] / binSize
    # x_axis = accumulatorArrays.shape[1] / binSize
    # z_axis = accumulatorArrays.shape[2] / binSize
    maximum = accumulatorArrays.max()
    lowerThresholdValue = lowerThreshold * maximum
    upperThresholdValue = upperThreshold * maximum
    accumulatorArrays[np.where(accumulatorArrays < lowerThresholdValue)] += maximum

    locations = np.where(accumulatorArrays < upperThresholdValue)
    centers = []
    for i in xrange(len(locations[0])):
        centers.append((locations[1][i], locations[0][i], locations[2][i]))
    return centers