from quantizeRGB import quantizeRGB
from quantizeHSV import quantizeHSV
from computeQuantizationError import computeQuantizationError
from getHueHists import getHueHists
from detectCircles import detectCircles
from detectAllCircles import detectAllCircles

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
plt.imshow(img)
plt.show()
radius = 108
# with gradient
# centers = detectCircles(img.copy(), radius, 1)
# print centers
# # plot circles
# fig = plt.figure()
# plt.imshow(img)
# circle = []
# for center in centers:
#     fig.add_subplot(111).add_artist(plt.Circle(center,radius,color=(1,0,0),fill=False))
# plt.show()
# without gradient
# centers = detectCircles(img.copy(), radius, 0)
# print centers
# # plot circles
# fig = plt.figure()
# plt.imshow(img)
# circle = []
# for center in centers:
#     fig.add_subplot(111).add_artist(plt.Circle(center,radius,color=(1,0,0),fill=False))
# plt.show()

centers = detectAllCircles(img.copy())
print centers
# plot circles
fig = plt.figure()
plt.imshow(img)
circle = []
for center in centers:
    fig.add_subplot(111).add_artist(plt.Circle((center[0],center[1]),center[2],color=(1,0,0),fill=False))
plt.show()