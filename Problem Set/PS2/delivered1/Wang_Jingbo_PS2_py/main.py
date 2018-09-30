from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from find_optimal_horizontal_seam import find_optimal_horizontal_seam
from displaySeam import displaySeam

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

### prague
img = mpimg.imread('./inputSeamCarvingPrague.jpg')
plt.imshow(img)
# plt.savefig('./energyImagePrague.png')
plt.show()

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

### mall
img = mpimg.imread('./inputSeamCarvingMall.jpg')
plt.imshow(img)
# plt.savefig('./energyImagePrague.png')
plt.show()

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
