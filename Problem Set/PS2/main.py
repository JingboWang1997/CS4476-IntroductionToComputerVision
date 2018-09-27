from energy_image import energy_image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage

# energyImage
img = mpimg.imread('./inputSeamCarvingPrague.jpg')
energyImage = energy_image(img)
plt.imshow(energyImage, cmap=plt.get_cmap('gray'))
plt.show()
