from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from find_optimal_horizontal_seam import find_optimal_horizontal_seam
from displaySeam import displaySeam
from reduceWidth import reduceWidth
from reduceHeight import reduceHeight

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage

img = mpimg.imread('./inputSeamCarvingPrague.jpg')

### energyImage
energyImage = energy_image(img)
plt.imshow(energyImage, cmap=plt.get_cmap('gray'))
# plt.savefig('./energyImagePrague.png')
plt.show()

### cumulative energy map
mapV = cumulative_minimum_energy_map(energyImage, "VERTICAL")
mapH = cumulative_minimum_energy_map(energyImage, "HORIZONTAL")
plt.imshow(mapV, cmap=plt.get_cmap('gray'))
# plt.savefig('./verticalCumulativeEnergyMapPrague.png')
plt.show()
plt.imshow(mapH, cmap=plt.get_cmap('gray'))
# plt.savefig('./horizontalCumulativeEnergyMapPrague.png')
plt.show()

### vertical seam
vSeam = find_optimal_vertical_seam(mapV)

### horizontal seam
hSeam = find_optimal_horizontal_seam(mapH)

### display seam
displaySeam(img, vSeam, "VERTICAL")
displaySeam(img, hSeam, "HORIZONTAL")

### reduced width
[reducedColorImage1, reducedEnergyImage1] = reduceWidth(img, energyImage)
[reducedColorImage2,reducedEnergyImage2] = reduceHeight(img, energyImage)
# plt.imshow(energyImage, cmap="gray")
# plt.show()
# plt.imshow(reducedEnergyImage2, cmap="gray")
# plt.show()
# plt.imshow(img)
# plt.show()
# plt.imshow(reducedColorImage2)
# plt.show()
