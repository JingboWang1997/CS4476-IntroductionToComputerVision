from quantizeRGB import quantizeRGB
from quantizeHSV import quantizeHSV
from computeQuantizationError import computeQuantizationError
from getHueHists import getHueHists
from detectCircles import detectCircles

import matplotlib.pyplot as plt

fishImg = plt.imread('./fish.jpg')

# color quantization with k-means
# a
# outputImg, meanColors = quantizeRGB(fishImg, 3)
# plt.imshow(outputImg)
# plt.show()
# print "mean colors: ", meanColors

# b
# outputImg, meanHues = quantizeHSV(fishImg, 3)
# plt.imshow(outputImg)
# plt.show()
# print "mean hues: ", meanHues

# c
# outputImg, meanColors = quantizeRGB(fishImg, 3)
# error = computeQuantizationError(fishImg,outputImg)
# print 'error: ', error

# d
# histEqual, histClustered = getHueHists(fishImg, 3)
# print histEqual
# plt.show(histEqual)
# plt.show(histClustered)

img = plt.imread('./egg.jpg')
radius = 5
centers = detectCircles(img, radius, 1)
print centers
centers = detectCircles(img, radius, 0)
print centers