import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def find_optimal_vertical_seam(cumulativeEnergyMap):
    seam = np.zeros((len(cumulativeEnergyMap),), int)
    seam[-1] = np.argmin(cumulativeEnergyMap[-1])

    # start tracing back from bottom
    for i in reversed(xrange(len(cumulativeEnergyMap) - 1)):
        curCol = seam[i + 1]

        # look at the three above (take care of edges)
        if (curCol - 1 >= 0 and curCol + 1 < len(cumulativeEnergyMap[0])):
            traceBackOptions = np.array([cumulativeEnergyMap[i][curCol - 1], cumulativeEnergyMap[i][curCol], cumulativeEnergyMap[i][curCol + 1]])
        elif (curCol - 1 < 0 and curCol + 1 < len(cumulativeEnergyMap[0])):
            traceBackOptions = np.array([float("inf"), cumulativeEnergyMap[i][curCol], cumulativeEnergyMap[i][curCol + 1]])
        elif (curCol + 1 >= len(cumulativeEnergyMap[0]) and curCol - 1 >= 0):
            traceBackOptions = np.array([cumulativeEnergyMap[i][curCol - 1], cumulativeEnergyMap[i][curCol], float("inf")])
        else:
            traceBackOptions = np.array([float("inf"), cumulativeEnergyMap[i][curCol], float("inf")])
        traceBackPointIndex = np.argmin(traceBackOptions)
        seam[i] = curCol + traceBackPointIndex - 1

    return seam

