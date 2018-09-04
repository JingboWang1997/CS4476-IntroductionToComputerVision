import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('./inputPS0Q2.jpg')

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# 1
swap = img.copy()
red = swap[:,:,0]
green = swap[:,:,1]
blue = swap[:,:,2]
temp = red.copy()
np.copyto(red, green)
np.copyto(green, temp)
plt.imshow(swap)
# plt.savefig('./swapImgPS0Q2.png')
plt.show()

# 2
rgb = img.copy()
gray = rgb2gray(rgb)
plt.imshow(gray, cmap = plt.get_cmap('gray'))
# plt.savefig('./grayImgPS0Q2.png')
plt.show()

# 3
# a
plt.imshow(gray, cmap = plt.get_cmap('gray_r'))
# plt.savefig('./negativeImgPS0Q2.png')
plt.show()

# b
image = gray.copy()
mirror = np.fliplr(image)
plt.imshow(mirror, cmap = plt.get_cmap('gray'))
# plt.savefig('./mirrorImgPS0Q2.png')
plt.show()

# c
original = gray.copy().astype(np.double)
mirror1 = np.fliplr(original).astype(np.double)
average = (original + mirror1) / 2
plt.imshow(average.astype(np.uint16), cmap = plt.get_cmap('gray'))
# plt.savefig('./avgImgPS0Q2.png')
plt.show()

# d
original = gray.copy()
noise = np.random.randint(0, 256, original.shape)
# np.save('./noise.npy', noise)
sum = original + noise
sum[sum > 255] = 255
plt.imshow(sum, cmap = plt.get_cmap('gray'))
# plt.savefig('./addNoiseImgPS0Q2.png')
plt.show()

# subplot
fig, axs = plt.subplots(3, 2)
axs[0, 0].imshow(swap)
axs[0, 0].set_title("1. Swap Red and Green Color Channels")
axs[0, 1].imshow(gray, cmap = plt.get_cmap('gray'))
axs[0, 1].set_title("2. Grayscale Image")
axs[1, 0].imshow(gray, cmap = plt.get_cmap('gray_r'))
axs[1, 0].set_title("3a. Negative Grayscale")
axs[1, 1].imshow(mirror, cmap = plt.get_cmap('gray'))
axs[1, 1].set_title("3b. Left and Right Mirrored Grayscale")
axs[2, 0].imshow(average.astype(np.uint16), cmap = plt.get_cmap('gray'))
axs[2, 0].set_title("3c. Average of Grayscale and Mirrored")
axs[2, 1].imshow(sum, cmap = plt.get_cmap('gray'))
axs[2, 1].set_title("3d. Grayscale with Noise")
fig.tight_layout()
plt.show()