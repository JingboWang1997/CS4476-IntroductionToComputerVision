from quantizeRGB import quantizeRGB
from quantizeHSV import quantizeHSV
from computeQuantizationError import computeQuantizationError
from getHueHists import getHueHists

import matplotlib.pyplot as plt

fishImg = plt.imread('./fish.jpg')
plt.imshow(fishImg)
plt.title("Original Image")
plt.show()
smallK = 3
largeK = 30

# color quantization with k-means
# rgb
outputImgRGB, meanColors = quantizeRGB(fishImg, smallK)
plt.imshow(outputImgRGB)
plt.title("Color Quantization in RGB (k = 3)")
plt.show()
print "Mean Colors (k = 3): ", meanColors
errorRGB = computeQuantizationError(fishImg, outputImgRGB)
print 'Error in RGB Space (k = 3): ', errorRGB

outputImgRGB, meanColors = quantizeRGB(fishImg, largeK)
plt.imshow(outputImgRGB)
plt.title("Color Quantization in RGB (k = 30)")
plt.show()
print "Mean colors (k = 30): ", meanColors
errorRGB = computeQuantizationError(fishImg, outputImgRGB)
print 'Error in RGB Space (k = 30): ', errorRGB

# hsv
outputImgHSV, meanHues = quantizeHSV(fishImg, 5)
plt.imshow(outputImgHSV)
plt.title("Color Quantization in HSV (k = 3)")
plt.show()
print "Mean Hues (k = 3): ", meanHues
errorHSV = computeQuantizationError(fishImg, outputImgHSV)
print 'Error in HSV Space (k = 3): ', errorHSV

outputImgHSV, meanHues = quantizeHSV(fishImg, largeK)
plt.imshow(outputImgHSV)
plt.title("Color Quantization in HSV (k = 30)")
plt.show()
print "Mean Hues (k = 30): ", meanHues
errorHSV = computeQuantizationError(fishImg, outputImgHSV)
print 'Error in HSV Space (k = 30): ', errorHSV

# histogram
histEqualSmall, histClusteredSmall = getHueHists(fishImg, smallK)
histEqualLarge, histClusteredLarge = getHueHists(fishImg, largeK)