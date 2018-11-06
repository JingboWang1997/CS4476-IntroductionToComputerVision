import glob
import scipy.io
import numpy as np
import operator
import math
import scipy.cluster.vq as vq
import random
import matplotlib.pyplot as plt
from scipy import misc
from skimage.color import rgb2gray

from getPatchFromSIFTParameters import getPatchFromSIFTParameters
from dist2 import dist2

def fullFrameQueries():
    # get three images
    dir = 'imageQueries/'
    queries = glob.glob(dir + '*.mat')
    querySifts = []
    for query in queries:
        querySifts.append(scipy.io.loadmat(query))

    # for each build a histogram
    for querySift in querySifts:
        # {image: similarity}
        similarityMap = {}

        queryHistogram = buildHistogram(querySift)
    #   loop through all the images
        imagesdir = '100sift/'
        imageNames = glob.glob(imagesdir + '*.mat')
        for imageName in imageNames:
            print imageName
            imageSift = scipy.io.loadmat(imageName)
    #       build a histogram on each
            imageHistogram = buildHistogram(imageSift)
    #       get similarity values
            similarity = getSimilarityValue(queryHistogram, imageHistogram)
            # put in {image: similarity} dictionary
            similarityMap[imageName] = similarity
    #   sort dictionary
        sorted_similarityMap = sorted(similarityMap.items(), key=operator.itemgetter(1))
        sorted_similarityMap.reverse()
    #   display top 5
        top5Images = []
        for m in range(5):
            name = sorted_similarityMap[m][0]
            name = name[-27:-4]
            top5Images.append(name)
        displayImageList(top5Images)




def buildHistogram(sift):
    descriptors = sift['descriptors']
    dictionary = np.load('./100vocabularies.npy')
    # initialize a 1500 length array
    histogram = np.zeros((len(dictionary),))
    # loop through all descriptors
    for descriptor in descriptors:
    #   find the index of the vocabulary
        index = findVocabIndex(descriptor, dictionary)
    #   array[index] += 1
        histogram[index] += 1
    return histogram

def getSimilarityValue(histogram1, histogram2):
    top = np.dot(histogram1, histogram2)
    l2norm1 = l2norm(histogram1)
    l2norm2 = l2norm(histogram2)
    if l2norm1 * l2norm2 == 0:
        return float('-inf')
    return top / (l2norm1 * l2norm2)

def findVocabIndex(descriptor, dictionary):
    descriptor = descriptor.reshape((1, 128))
    # entry = dist2(x,c)
    # entry[i][j] corresponds to the distance between x[i] and c[j]
    dist = dist2(descriptor, dictionary)
    return np.argmin(dist)

def l2norm(array):
    squared = 0
    for num in array:
        squared += (num ** 2)
    return math.sqrt(squared)

def displayImageList(imageList):
    dir = '100frames/'
    for image in imageList:
        img = misc.imread(dir + image)
        plt.imshow(img)
        plt.show()





fullFrameQueries()
