import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from computeH import computeH
from warpImage import warpImage

# crop
input = mpimg.imread('./crop1.jpg')
ref = mpimg.imread('./crop2.jpg')
points1 = np.load('./cc1.npy')
points2 = np.load('./cc2.npy')
H = computeH(points1.transpose(), points2.transpose())
# verify homography matrix
#   blue dot: original points on image
#   red dot: transformed points from another image
plt.imshow(ref)
plt.plot(points2.transpose()[0], points2.transpose()[1], "bo")
homogeneous = np.concatenate((points1.transpose(), [np.ones(points1.shape[0])]))
transformed = np.matmul(H, homogeneous)
plt.plot(transformed[0]/transformed[2], transformed[1]/transformed[2], "ro")
plt.show()

warpIm, mergeIm = warpImage(input, ref, H)
plt.imshow(warpIm)
plt.show()
plt.imshow(mergeIm)
plt.show()

# wdc
input = mpimg.imread('./wdc1.jpg')
ref = mpimg.imread('./wdc2.jpg')
points = np.load('./points.npy')
points1 = points[:, 0]
points2 = points[:, 1]
# selected points
plt.imshow(input)
plt.plot(points1[0], points1[1], "bo")
plt.show()
plt.imshow(ref)
plt.plot(points2[0], points2[1], "bo")
plt.show()

H = computeH(points1, points2)
warpIm, mergeIm = warpImage(input, ref, H)
plt.imshow(warpIm)
plt.show()
plt.imshow(mergeIm)
plt.show()

# my dorm image mosaic
input = mpimg.imread('./dorm1.jpg')
ref = mpimg.imread('./dorm2.jpg')
points = np.load('./selectPoints_Dorm.npy')
points1 = points[:, 0]
points2 = points[:, 1]
H = computeH(points1, points2)
warpIm, mergeIm = warpImage(input, ref, H)
plt.imshow(warpIm)
plt.show()
plt.imshow(mergeIm)
plt.show()

# warp into frame region
input = mpimg.imread('./content.jpg')
ref = mpimg.imread('./frame.jpg')
points = np.load('./selectPoints_Frame.npy')
points1 = points[:, 0]
points2 = points[:, 1]
H = computeH(points2, points1)
warpIm, mergeIm = warpImage(input, ref, H)
plt.imshow(warpIm)
plt.show()
plt.imshow(mergeIm)
plt.show()