import scipy.cluster.vq as vq

def quantizeRGB(origImg, k):
    # resize image to a 2-dimensional for kmeans2
    origImgResize = origImg.copy()
    origImgResize.resize((origImg.shape[0] * origImg.shape[1], origImg.shape[2]))
    # calculate kmeans
    centroid, label = vq.kmeans2(origImgResize.astype(float), k)
    # modify pixels to their closest centers
    origImgCluster = origImg.copy()
    for i in xrange(len(origImg)):
        for j in xrange(len(origImg[i])):
            origImgCluster[i,j] = centroid[label[(i * len(origImg[i])) + j]]
    return origImgCluster, centroid
