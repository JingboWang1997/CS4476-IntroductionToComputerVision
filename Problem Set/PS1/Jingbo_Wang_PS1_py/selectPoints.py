from matplotlib import pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# select points from image 1
def onclick1(event):
    # print('==================================')
    # print('image 1 select: xdata=%f, ydata=%f' % (event.xdata, event.ydata))
    point = np.array([event.xdata, event.ydata])
    pts1.append(point)
    # print "image 1 points selected: ", pts1
    # points1 = np.vstack(tuple(pts1))
    # print "image 1 points selected in 2xN format with x-axis on the first row and y-axis on the second row: "
    # print points1.transpose()
    # np.save('./points1', points1.transpose())

# select points from image 2
def onclick2(event):
    # print('==================================')
    # print('image 2 select: x=%d, y=%d, xdata=%f, ydata=%f' % (event.x, event.y, event.xdata, event.ydata))
    point = np.array([event.xdata, event.ydata])
    pts2.append(point)
    # print "image 2 points selected: ", pts2
    # points2 = np.vstack(tuple(pts2))
    # print "image 2 points selected in 2xN format with x-axis on the first row and y-axis on the second row: "
    # print points2.transpose()
    # np.save('./points2', points2.transpose())

# specify the 2 images to select corresponding points from
img1 = './dorm1.jpg'
img2 = './dorm2.jpg'

pts1 = []
pts2 = []

# select on the first image
# print "Select Points on First Image"
img = mpimg.imread(img1)
implot = plt.imshow(img)
cid1 = implot.figure.canvas.mpl_connect('button_press_event', onclick1)
plt.show()

# select on the second image
# print "Select Points on Second Image"
img = mpimg.imread(img2)
implot = plt.imshow(img)
cid2 = implot.figure.canvas.mpl_connect('button_press_event', onclick2)
plt.show()

# construct final selection result
points1 = np.vstack(tuple(pts1)).transpose()
points2 = np.vstack(tuple(pts2)).transpose()
points = np.array([[points1[0], points2[0]], [points1[1], points2[1]]])
# print('==================================')
# print "Finished Selecting Points:"
# print "points1: ", points1
# print "points2: ", points2
# print "points1 on first column and points2 on second column:"
# print points

# save the selected points in a file
# name = 'selectPoints.npy'
# url = './' + name
# np.save(url, points)
# print "saved to a file named: ", name