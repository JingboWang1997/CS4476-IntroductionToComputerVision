import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def find_optimal_vertical_seam(cumulativeEnergyMap):
    seam = np.zeros((len(cumulativeEnergyMap),))