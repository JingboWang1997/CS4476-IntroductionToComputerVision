import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def find_optimal_horizontal_seam(cumulativeEnergyMap):
    seam = np.zeros((len(cumulativeEnergyMap[0]),), int)
    seam[-1] = np.argmin(cumulativeEnergyMap[:, len(cumulativeEnergyMap[0]) - 1])

    # start tracing back from right (take care of edges)
    for i in reversed(xrange(len(cumulativeEnergyMap[0]) - 1)):
        curRow = seam[i + 1]
        # look at the three left
        if (curRow - 1 >= 0 and curRow + 1 < len(cumulativeEnergyMap)):
            traceBackOptions = np.array([cumulativeEnergyMap[curRow - 1][i], cumulativeEnergyMap[curRow][i], cumulativeEnergyMap[curRow + 1][i]])
        elif (curRow - 1 < 0 and curRow + 1 < len(cumulativeEnergyMap)):
            traceBackOptions = np.array([float("inf"), cumulativeEnergyMap[curRow][i], cumulativeEnergyMap[curRow + 1][i]])
        elif (curRow + 1 >= len(cumulativeEnergyMap) and curRow - 1 >= 0):
            traceBackOptions = np.array([cumulativeEnergyMap[curRow - 1][i], cumulativeEnergyMap[curRow][i], float("inf")])
        else:
            traceBackOptions = np.array([float("inf"), cumulativeEnergyMap[curRow][i], float("inf")])
        traceBackPointIndex = np.argmin(traceBackOptions)
        seam[i] = curRow + traceBackPointIndex - 1

    return seam