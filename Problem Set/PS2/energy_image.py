import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

def energy_image(im):
    bw = rgb2gray(im)
    kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    # Perform gradient
    x = np.absolute(ndimage.convolve(bw, kernelx)).astype(np.double)
    # Perform y convolution
    y = np.absolute(ndimage.convolve(bw, kernely)).astype(np.double)
    # add the two gradient together
    result = x + y

    # plt.imshow(x, cmap = plt.get_cmap('gray'))
    # plt.show()
    # plt.imshow(y, cmap=plt.get_cmap('gray'))
    # plt.show()
    # plt.imshow(result, cmap=plt.get_cmap('gray'))
    # plt.show()

    return result

img = mpimg.imread('./inputSeamCarvingPrague.jpg')
energy_image(img)
