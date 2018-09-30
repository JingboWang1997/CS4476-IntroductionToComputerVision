from energy_image import energy_image
from reduceWidth import reduceWidth
from progressBar import progress

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

### prague image
imgPrague = mpimg.imread('./inputSeamCarvingPrague.jpg')
energyImagePrague = energy_image(imgPrague)

for i in xrange(100):
    # progress(i, 100, status="reducing prague image width by 100")
    [imgPrague, energyImagePrague] = reduceWidth(imgPrague, energyImagePrague)

plt.imshow(imgPrague)
# plt.savefig('./outputReduceWidthPrague.png')
plt.show()

### mall image
imgMall = mpimg.imread('./inputSeamCarvingMall.jpg')
energyImageMall = energy_image(imgMall)

for i in xrange(100):
    # progress(i, 100, status="reducing mall image width by 100")
    [imgMall, energyImageMall] = reduceWidth(imgMall, energyImageMall)

plt.imshow(imgMall)
# plt.savefig('./outputReduceWidthMall.png')
plt.show()