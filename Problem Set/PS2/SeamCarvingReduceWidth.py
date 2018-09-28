from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from reduceWidth import reduceWidth
from progressBar import progress

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

### prague image
imgPrague = mpimg.imread('./inputSeamCarvingPrague.jpg')
### energyImage
energyImagePrague = energy_image(imgPrague)

originalEnergyPrague = energyImagePrague.copy()
originalImagePrague = imgPrague.copy()

for i in xrange(100):
    progress(i, 100, status="reducing prague image width by 100")
    ### cumulative energy map
    mapV = cumulative_minimum_energy_map(energyImagePrague, "VERTICAL")
    ### vertical seam
    vSeam = find_optimal_vertical_seam(mapV)
    ### reduce width
    [imgPrague, energyImagePrague] = reduceWidth(imgPrague, energyImagePrague)

plt.imshow(originalEnergyPrague, cmap="gray")
plt.show()
plt.imshow(energyImagePrague, cmap="gray")
plt.show()
plt.imshow(originalImagePrague)
plt.show()
plt.imshow(imgPrague)
plt.show()

### mall image
imgMall = mpimg.imread('./inputSeamCarvingMall.jpg')
### energyImage
energyImageMall = energy_image(imgMall)

originalEnergyMall = energyImageMall.copy()
originalImageMall = imgMall.copy()

for i in xrange(100):
    progress(i, 100, status="reducing mall image width by 100")
    ### cumulative energy map
    mapV = cumulative_minimum_energy_map(energyImageMall, "VERTICAL")
    ### vertical seam
    vSeam = find_optimal_vertical_seam(mapV)
    ### reduce width
    [imgMall, energyImageMall] = reduceWidth(imgMall, energyImageMall)

plt.imshow(originalEnergyMall, cmap="gray")
plt.show()
plt.imshow(energyImageMall, cmap="gray")
plt.show()
plt.imshow(originalImageMall)
plt.show()
plt.imshow(imgMall)
plt.show()
