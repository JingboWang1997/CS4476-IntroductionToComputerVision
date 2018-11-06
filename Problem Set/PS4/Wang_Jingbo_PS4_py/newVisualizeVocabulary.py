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
    framedir = '100frames/'
    # Get a list of all the .mat file in that directory.
    # there is one .mat file per image.
    fnames = glob.glob(siftdir + '*.mat')
    framenames = glob.glob(framedir + '*.jpeg')

    # only create new vocabs when needed
    if newVocab:
        # get all descrptors
        allDescriptors = np.empty((0, 128))
        for fname in fnames:
            print fname
            mat = scipy.io.loadmat(fname)
            # ['numfeats', 'orients', 'scales', 'descriptors', '__header__',
            # '__globals__', 'positions', '__version__', 'corners', 'imname']
            allDescriptors = np.vstack((allDescriptors, mat['descriptors']))
        print allDescriptors.shape
        # centroid = vocabularies, label = which vocabulary each one belongs to in original
        centroid, label = vq.kmeans2(allDescriptors, 1500)
        np.save('./100vocabularies.npy', centroid)
        np.save('./labels.npy', label)

    dictionary = np.load('./100vocabularies.npy')
    labels = np.load('./labels.npy') # same length as total sift

    # select two vocabularies that are at least over 25 occurrences
    occurencesList = np.bincount(labels)
    indexList = np.where(occurencesList >= 25)[0]
    [vocabIndex1, vocabIndex2] = random.sample(indexList, 2)
    vocab1Location = np.where(labels == vocabIndex1)[0][0:25]
    vocab2Location = np.where(labels == vocabIndex2)[0][0:25]

    # contain (patchIndex, mat, img)
    patches1 = []
    patches2 = []

    startPos = 0
    # traverse through images
    for index in range(len(fnames)):
        currentFrame = scipy.io.loadmat(fnames[index])
        currentImage = misc.imread(framenames[index])

        # set frame
        descriptors = currentFrame['descriptors']
        endPos = startPos + len(descriptors)

        # get indices
        patches1Indices = vocab1Location[np.where(vocab1Location >= startPos)]
        patches1Indices = patches1Indices[np.where(patches1Indices < endPos)]
        patches2Indices = vocab2Location[np.where(vocab2Location >= startPos)]
        patches2Indices = patches2Indices[np.where(patches2Indices < endPos)]

        # put the indices in the patches list
        for patchIndex in patches1Indices:
            patches1.append((patchIndex - startPos, currentFrame, currentImage))
        for patchIndex in patches2Indices:
            patches2.append((patchIndex - startPos, currentFrame, currentImage))
        startPos += len(descriptors)

    fig, axs = plt.subplots(5, 5)
    # traverse through pathches1 to display
    plotCounter = 0
    for (patchIndex, mat, img) in patches1:
        img_patch = getPatchFromSIFTParameters(mat['positions'][patchIndex, :], mat['scales'][patchIndex],
                                               mat['orients'][patchIndex], rgb2gray(img))
        row = int(plotCounter / 5)
        col = int(plotCounter % 5)
        axs[row, col].imshow(img_patch, cmap = "gray")
        plotCounter += 1
    plt.show()

    fig, axs = plt.subplots(5, 5)
    # traverse through pathches2 to display
    plotCounter = 0
    for (patchIndex, mat, img) in patches2:
        img_patch = getPatchFromSIFTParameters(mat['positions'][patchIndex, :], mat['scales'][patchIndex],
                                               mat['orients'][patchIndex], rgb2gray(img))
        row = int(plotCounter / 5)
        col = int(plotCounter % 5)
        axs[row, col].imshow(img_patch, cmap="gray")
        plotCounter += 1
    plt.show()

visualizeVocabulary()