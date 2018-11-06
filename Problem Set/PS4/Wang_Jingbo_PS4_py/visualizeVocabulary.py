import glob
import scipy.io
import numpy as np
import scipy.cluster.vq as vq
import random
import matplotlib.pyplot as plt
from scipy import misc
from skimage.color import rgb2gray

from getPatchFromSIFTParameters import getPatchFromSIFTParameters
from dist2 import dist2

def visualizeVocabulary(newVocab = False):
    # specific siftdir
    siftdir = '100sift/'
    # Get a list of all the .mat files
    fnames = glob.glob(siftdir + '*.mat')

    # only create new vocabs when needed
    if newVocab:
        # get all descriptors
        allDescriptors = np.empty((0, 128))
        for fname in fnames:
            print fname
            mat = scipy.io.loadmat(fname)
            # keys
            # ['numfeats', 'orients', 'scales', 'descriptors', '__header__',
            # '__globals__', 'positions', '__version__', 'corners', 'imname']
            allDescriptors = np.vstack((allDescriptors, mat['descriptors']))
        # centroid = vocabularies, label = which vocabulary each one belongs to in the original list
        centroid, label = vq.kmeans2(allDescriptors, 1500)
        np.save('./100vocabularies.npy', centroid)
        np.save('./labels.npy', label)

    # load in dictionary
    dictionary = np.load('./100vocabularies.npy')
    # select two vocabularies
    [vocab1, vocab2] = random.sample(dictionary, 2)

    # iterate through sift to put (imageIndex, patchIndex) that belong to the chosen vocabulary
    patches1 = []
    patches2 = []
    imageIndex = 0
    while (len(patches1) < 25 or len(patches2) < 25) and imageIndex < len(fnames):
        print fnames[imageIndex]
        mat = scipy.io.loadmat(fnames[imageIndex])
        # ['numfeats', 'orients', 'scales', 'descriptors', '__header__',
        # '__globals__', 'positions', '__version__', 'corners', 'imname']

        # iterate through all descriptors
        for patchIndex in range(len(mat['descriptors'])):
            if isPatchVocab(mat['descriptors'][patchIndex], dictionary, vocab1) and len(patches1) < 25:
                patches1.append((imageIndex, patchIndex))
                print "patches 1: " + str(len(patches1))
            elif isPatchVocab(mat['descriptors'][patchIndex], dictionary, vocab2) and len(patches2) < 25:
                patches2.append((imageIndex, patchIndex))
                print "patches 2: " + str(len(patches2))
        imageIndex += 1

    # get all images
    framedir = '100frames/'
    framenames = glob.glob(framedir + '*.jpeg')

    fig, axs = plt.subplots(5, 5)
    # traverse through pathches1 to display
    plotCounter = 0
    for imageIndex, patchIndex in patches1:
        currentFrame = misc.imread(framenames[imageIndex])
        currentsift = scipy.io.loadmat(fnames[imageIndex])
        img_patch = getPatchFromSIFTParameters(currentsift['positions'][patchIndex, :], currentsift['scales'][patchIndex],
                                               currentsift['orients'][patchIndex], rgb2gray(currentFrame))
        row = int(plotCounter / 5)
        col = int(plotCounter % 5)
        axs[row, col].imshow(img_patch, cmap = "gray")
        plotCounter += 1
    plt.show()

    fig, axs = plt.subplots(5, 5)
    # traverse through pathches2 to display
    plotCounter = 0
    for imageIndex, patchIndex in patches2:
        currentFrame = misc.imread(framenames[imageIndex])
        currentsift = scipy.io.loadmat(fnames[imageIndex])
        img_patch = getPatchFromSIFTParameters(currentsift['positions'][patchIndex, :],
                                               currentsift['scales'][patchIndex],
                                               currentsift['orients'][patchIndex], rgb2gray(currentFrame))
        row = int(plotCounter / 5)
        col = int(plotCounter % 5)
        axs[row, col].imshow(img_patch, cmap="gray")
        plotCounter += 1
    plt.show()

def isPatchVocab(descriptor, dictionary, vocab):
    descriptor = descriptor.reshape((1,128))
    # entry = dist2(x,c)
    # entry[i][j] corresponds to the distance between x[i] and c[j]
    dist = dist2(descriptor, dictionary)
    index = np.argmin(dist)
    lookup = dictionary[index]
    return np.array_equal(lookup, vocab)



visualizeVocabulary()