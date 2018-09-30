from energy_image import energy_image
from reduceHeight import reduceHeight
from progressBar import progress

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

### prague image
imgPrague = mpimg.imread('./inputSeamCarvingPrague.jpg')
energyImagePrague = energy_image(imgPrague)
for i in xrange(100):
    # progress(i, 100, status="reducing prague image height by 100")
    [imgPrague, energyImagePrague] = reduceHeight(imgPrague, energyImagePrague)
plt.imshow(imgPrague)
# plt.savefig('./outputReduceHeightPrague.png')
plt.show()

### mall image
imgMall = mpimg.imread('./inputSeamCarvingMall.jpg')
energyImageMall = energy_image(imgMall)
for i in xrange(100):
    # progress(i, 100, status="reducing mall image width by 100")
    ### reduce width
    [imgMall, energyImageMall] = reduceHeight(imgMall, energyImageMall)
plt.imshow(imgMall)
# plt.savefig('./outputReduceHeightMall.png')
plt.show()