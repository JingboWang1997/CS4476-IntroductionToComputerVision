from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage

img = mpimg.imread('./inputSeamCarvingPrague.jpg')

### energyImage
energyImage = energy_image(img)
plt.imshow(energyImage, cmap=plt.get_cmap('gray'))
plt.show()

### cumulative energy map
mapV = cumulative_minimum_energy_map(energyImage, "VERTICAL")
mapH = cumulative_minimum_energy_map(energyImage, "HORIZONTAL")
# plt.imshow(mapV, cmap=plt.get_cmap('gray'))
# plt.show()
# plt.imshow(mapH, cmap=plt.get_cmap('gray'))
# plt.show()

### vertical seam
find_optimal_vertical_seam(mapV)
