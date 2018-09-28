from find_optimal_vertical_seam import find_optimal_vertical_seam
from cumulative_minimum_energy_map import cumulative_minimum_energy_map

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def reduceWidth(im, energyImage):
    mapV = cumulative_minimum_energy_map(energyImage, "VERTICAL")
    seam = find_optimal_vertical_seam(mapV)

    newIm = np.zeros((im.shape[0], im.shape[1]-1, im.shape[2])).astype(int)
    newEnergyImage = np.zeros((energyImage.shape[0], energyImage.shape[1]-1))

    for i in xrange(len(seam)):
        newIm[i] = np.delete(im[i], seam[i], 0)
        newEnergyImage[i] = np.delete(energyImage[i], seam[i])

    return [newIm, newEnergyImage]
