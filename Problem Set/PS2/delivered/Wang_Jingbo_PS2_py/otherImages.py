from energy_image import energy_image
from reduceWidth import reduceWidth
from reduceHeight import reduceHeight
from progressBar import progress

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc

### image
filename = 'face.jpg'
foldername = 'face'
img = mpimg.imread('./more images/' + filename)
plt.imshow(img)
# plt.savefig('./more images/'+ foldername + '/original.png')
energyImage = energy_image(img)
halfWidth = img.shape[1] / 2
oneFifthWidth = img.shape[1] / 5
halfHeight = img.shape[0] / 2
oneFifthHeight = img.shape[0] / 5

# reduce 1/2 width and 1/5 height
systemResize = misc.imresize(img, (img.shape[0] - oneFifthHeight, img.shape[1] - halfWidth, 3))
plt.imshow(systemResize)
# plt.savefig('./more images/'+ foldername + '/12w15hNormalResize.png')
plt.show()
# horizontal and then vertical
for i in xrange(oneFifthHeight):
    # progress(i, oneFifthHeight, status="reducing image by 1/5 height")
    [img, energyImage] = reduceHeight(img, energyImage)
for i in xrange(halfWidth):
    # progress(i, halfWidth, status="reducing image by 1/2 width")
    [img, energyImage] = reduceWidth(img, energyImage)
plt.imshow(img)
# plt.savefig('./more images/'+ foldername + '/12w15hHVResize.png')
plt.show()
# vertical and then horizontal
img = mpimg.imread('./more images/' + filename)
energyImage = energy_image(img)
for i in xrange(halfWidth):
    # progress(i, halfWidth, status="reducing image by 1/2 width")
    [img, energyImage] = reduceWidth(img, energyImage)
for i in xrange(oneFifthHeight):
    # progress(i, oneFifthHeight, status="reducing image by 1/5 height")
    [img, energyImage] = reduceHeight(img, energyImage)
plt.imshow(img)
# plt.savefig('./more images/'+ foldername + '/12w15hVHResize.png')
plt.show()
# alternate V and H
img = mpimg.imread('./more images/' + filename)
energyImage = energy_image(img)
widthCounter = 0
heightCounter = 0
current = "V"
for i in xrange(halfWidth + oneFifthHeight):
    # progress(i, halfWidth + oneFifthHeight, status="reducing image by 1/2 width and 1/5 height")
    if (current == "V" and widthCounter < halfWidth):
        [img, energyImage] = reduceWidth(img, energyImage)
        current = "H"
        widthCounter += 1
    elif (current == "H" and heightCounter < oneFifthHeight):
        [img, energyImage] = reduceHeight(img, energyImage)
        current = "V"
        heightCounter += 1
    elif (heightCounter >= oneFifthHeight):
        [img, energyImage] = reduceWidth(img, energyImage)
    else:
        [img, energyImage] = reduceHeight(img, energyImage)
plt.imshow(img)
# plt.savefig('./more images/'+ foldername + '/12w15hAltResize.png')
plt.show()

# reduce 1/5 width and 1/2 height
img = mpimg.imread('./more images/' + filename)
energyImage = energy_image(img)
systemResize = misc.imresize(img, (img.shape[0] - halfHeight, img.shape[1] - oneFifthWidth, 3))
plt.imshow(systemResize)
# plt.savefig('./more images/'+ foldername + '/15w12NormalResize.png')
plt.show()
# horizontal and then vertical
for i in xrange(halfHeight):
    # progress(i, halfHeight, status="reducing image by 1/2 height")
    [img, energyImage] = reduceHeight(img, energyImage)
for i in xrange(oneFifthWidth):
    # progress(i, oneFifthWidth, status="reducing image by 1/5 width")
    [img, energyImage] = reduceWidth(img, energyImage)
plt.imshow(img)
# plt.savefig('./more images/'+ foldername + '/15w12hHVResize.png')
plt.show()
# vertical and then horizontal
img = mpimg.imread('./more images/' + filename)
energyImage = energy_image(img)
for i in xrange(oneFifthWidth):
    # progress(i, oneFifthWidth, status="reducing image by 1/5 width")
    [img, energyImage] = reduceWidth(img, energyImage)
for i in xrange(halfHeight):
    # progress(i, halfHeight, status="reducing image by 1/2 height")
    [img, energyImage] = reduceHeight(img, energyImage)
plt.imshow(img)
# plt.savefig('./more images/'+ foldername + '/15w12hVHResize.png')
plt.show()
# alternate H and V
img = mpimg.imread('./more images/' + filename)
energyImage = energy_image(img)
widthCounter = 0
heightCounter = 0
current = "H"
for i in xrange(oneFifthWidth + halfHeight):
    # progress(i, oneFifthWidth + halfHeight, status="reducing image by 1/5 width and 1/2 height")
    if (current == "V" and widthCounter < oneFifthWidth):
        [img, energyImage] = reduceWidth(img, energyImage)
        current = "H"
        widthCounter += 1
    elif (current == "H" and heightCounter < halfHeight):
        [img, energyImage] = reduceHeight(img, energyImage)
        current = "V"
        heightCounter += 1
    elif (heightCounter >= halfHeight):
        [img, energyImage] = reduceWidth(img, energyImage)
    else:
        [img, energyImage] = reduceHeight(img, energyImage)
plt.imshow(img)
# plt.savefig('./more images/'+ foldername + '/15w12hAltResize.png')
plt.show()