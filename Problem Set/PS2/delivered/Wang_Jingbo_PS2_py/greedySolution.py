from energy_image import energy_image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def greedy(energyImage, seamDirection):
    if (seamDirection == "VERTICAL"):
        seam = np.zeros((len(energyImage),), int)
        seam[0] = np.argmin(energyImage[0])
        # start tracing
        for i in xrange(1, len(energyImage)):
            curCol = seam[i - 1]
            # look at the three lower
            if (curCol - 1 >= 0 and curCol + 1 < len(energyImage[0])):
                traceOptions = np.array([energyImage[i][curCol - 1], energyImage[i][curCol], energyImage[i][curCol + 1]])
            elif (curCol - 1 < 0 and curCol + 1 < len(energyImage[0])):
                traceOptions = np.array([float("inf"), energyImage[i][curCol], energyImage[i][curCol + 1]])
            elif (curCol + 1 >= len(energyImage[0]) and curCol - 1 >= 0):
                traceOptions = np.array([energyImage[i][curCol - 1], energyImage[i][curCol], float("inf")])
            else:
                traceOptions = np.array([float("inf"), energyImage[i][curCol], float("inf")])
            tracePointIndex = np.argmin(traceOptions)
            seam[i] = curCol + tracePointIndex - 1
        return seam
    elif (seamDirection == "HORIZONTAL"):
        seam = np.zeros((len(energyImage[0]),), int)
        seam[0] = np.argmin(energyImage[:, 0])

        # start tracing
        for i in xrange(1, len(energyImage[0])):
            curRow = seam[i - 1]
            # look at the three right
            if (curRow - 1 >= 0 and curRow + 1 < len(energyImage)):
                traceOptions = np.array([energyImage[curRow - 1][i], energyImage[curRow][i], energyImage[curRow + 1][i]])
            elif (curRow - 1 < 0 and curRow + 1 < len(energyImage)):
                traceOptions = np.array([float("inf"), energyImage[curRow][i], energyImage[curRow + 1][i]])
            elif (curRow + 1 >= len(energyImage) and curRow - 1 >= 0):
                traceOptions = np.array([energyImage[curRow - 1][i], energyImage[curRow][i], float("inf")])
            else:
                traceOptions = np.array([float("inf"), energyImage[curRow][i], float("inf")])
            tracePointIndex = np.argmin(traceOptions)
            seam[i] = curRow + tracePointIndex - 1
        return seam
    return None

### vertical
originalImg = mpimg.imread('./inputSeamCarvingPrague.jpg')
img = originalImg.copy()
for i in xrange(100):
    energyImage = energy_image(img)
    seam = greedy(energyImage, "VERTICAL")
    plt.imshow(energyImage, cmap="gray")
    if i == 0:
        for i in xrange(len(seam)):
            plt.plot(seam[i], i, 'r,')
        plt.show()
    newIm = np.zeros((img.shape[0], img.shape[1]-1, img.shape[2])).astype(int)
    newEnergyImage = np.zeros((energyImage.shape[0], energyImage.shape[1]-1))
    for i in xrange(len(seam)):
        newIm[i] = np.delete(img[i], seam[i], 0)
    img = newIm
plt.imshow(originalImg)
plt.show()
plt.imshow(img)
plt.show()

### horizontal
img = originalImg.copy()
for i in xrange(100):
    energyImage = energy_image(img)
    seam = greedy(energyImage, "HORIZONTAL")
    plt.imshow(energyImage, cmap="gray")
    if i == 0:
        for i in xrange(len(seam)):
            plt.plot(i, seam[i], 'r,')
        plt.show()
    newIm = np.zeros((img.shape[0]-1, img.shape[1], img.shape[2])).astype(int)
    newEnergyImage = np.zeros((energyImage.shape[0]-1, energyImage.shape[1]))
    for i in xrange(len(seam)):
        newIm[:, i] = np.delete(img[:, i], seam[i], 0)
    img = newIm
plt.imshow(originalImg)
plt.show()
plt.imshow(img)
plt.show()