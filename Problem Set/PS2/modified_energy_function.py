from energy_image import energy_image
from reduceWidth import reduceWidth
from progressBar import progress

import numpy as np
from scipy import ndimage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

def energy_image_simple(im):
    bw = rgb2gray(im)
    # use simple one line derivative filters
    kernely = np.array([[1], [0], [-1]])
    kernelx = np.array([[-1, 0, 1]])
    # Perform x convolution
    x = np.absolute(ndimage.convolve(bw, kernelx))
    # Perform y convolution
    y = np.absolute(ndimage.convolve(bw, kernely))
    # add the two gradient together
    result = x + y
    return result.astype(np.double)

def energy_image_high_threshold(im):
    bw = rgb2gray(im)
    # use prewitt filters
    kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    # Perform x convolution
    y = np.absolute(ndimage.convolve(bw, kernely))
    # take threshold
    threshold = np.mean(y)
    y -= threshold
    return y

### simple derivative
imgModify = mpimg.imread('./inputSeamCarvingPrague.jpg')
img = imgModify.copy()
modifiedEnergyImage = energy_image_simple(img)
energyImage = energy_image(img)
plt.imshow(energyImage, cmap=plt.get_cmap('gray'))
plt.show()
plt.imshow(modifiedEnergyImage, cmap=plt.get_cmap('gray'))
plt.show()
for i in xrange(100):
    progress(i, 100, status="reducing prague image width by 100 with simple one row derivative")
    [imgModify, modifiedEnergyImage] = reduceWidth(imgModify, modifiedEnergyImage)
    [img, energyImage] = reduceWidth(img, energyImage)
plt.imshow(img)
plt.show()
plt.imshow(imgModify)
plt.show()

### take a high threshold cutoff
imgModify = mpimg.imread('./inputSeamCarvingPrague.jpg')
img = imgModify.copy()
modifiedEnergyImage = energy_image_high_threshold(img)
energyImage = energy_image(img)
plt.imshow(energyImage, cmap=plt.get_cmap('gray'))
plt.show()
plt.imshow(modifiedEnergyImage, cmap=plt.get_cmap('gray'))
plt.show()
for i in xrange(100):
    progress(i, 100, status="reducing prague image width by 100 with a threshold cutoff")
    [imgModify, modifiedEnergyImage] = reduceWidth(imgModify, modifiedEnergyImage)
    [img, energyImage] = reduceWidth(img, energyImage)
plt.imshow(img)
plt.show()
plt.imshow(imgModify)
plt.show()