import numpy as np

def computeQuantizationError(origImg,quantizedImg):
    # take difference (error)
    diff = origImg - quantizedImg
    # take square (squared error)
    squared = np.square(diff)
    # take sum (sum of squared error
    sum = np.sum(squared)
    return sum