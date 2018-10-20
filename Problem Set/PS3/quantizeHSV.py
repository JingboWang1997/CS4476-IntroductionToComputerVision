from skimage import color
import scipy.cluster.vq as vq
import numpy as np

def quantizeHSV(origImg, k):
    # convert to hsv
    origImgHSV = color.rgb2hsv(origImg)
    # take hue array
    hueSpace = origImgHSV[:,:,0].copy()
    hueSpace.resize((hueSpace.shape[0] * hueSpace.shape[1],))
    # take kmeans
    centroid, label = vq.kmeans2(hueSpace.astype(float), k)

    # input new hue
    for i in xrange(len(origImgHSV)):
        for j in xrange(len(origImgHSV[i])):
            origImgHSV[i,j,0] = centroid[label[(i * len(origImgHSV[i])) + j]]
    # convert to rgb with uint8
    outputImg = color.hsv2rgb(origImgHSV)
    outputImg = (outputImg * 255).astype(np.uint8)
    return outputImg, centroid