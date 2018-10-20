import numpy as np
from skimage import color
import scipy.cluster.vq as vq
import matplotlib.pyplot as plt

def getHueHists(im, k):
    # take hue kmeans
    origImgHSV = color.rgb2hsv(im)
    hueSpace = origImgHSV[:, :, 0].copy()
    hueSpace.resize((hueSpace.shape[0] * hueSpace.shape[1],))
    centroid, label = vq.kmeans2(hueSpace.astype(float), k)

    # cluster points into k clusters
    clusters = []
    for i in xrange(k):
        clusters.append([])
    for i in xrange(len(label)):
        clusters[label[i]].append(hueSpace[i])
    # print clusters
    # for i in xrange(len(clusters)):
    #     if (len(clusters[i]) == 0):
    #         print 'cluster ', i, ': ', len(clusters[i])
    #     else:
    #         print 'cluster ', i, '[', min(clusters[i]), ' : ', max(clusters[i]), ']: ', len(clusters[i])

    # use the clusters to calculate edges
    #   min of each cluster as lower bound and upper bound for the previous one
    edges = []
    counter = 0
    for i in xrange(k):
        print 'cluster: ', len(clusters[i])
        if (len(clusters[i]) == 0):
            counter += 1
        edges.append([])
        if (len(clusters[i]) == 0):
            # this is to handle empty cluster cases
            edges[i] = 0 if (i == 0) else edges[i-1]
        else:
            edges[i] = min(clusters[i])
    # take max of entire set as the right-most bound
    edges.append([])
    edges[k] = max(hueSpace)
    edges.sort()

    # construct equal bin histogram
    histEqual = plt.hist(hueSpace, k, edgecolor='black')
    plt.title("Hue Equal Bin Histogram (with k = " + str(k) + ")")
    plt.show(histEqual)

    # construct clustered bin histogram
    histClustered = plt.hist(hueSpace, bins=edges, edgecolor='black')
    plt.title("Hue Clustered Bin Histogram (with k = " + str(k) + ")")
    plt.show(histClustered)

    return histEqual, histClustered