from detectCircles import detectCircles
from detectAllCircles import detectAllCircles

import matplotlib.pyplot as plt

img = plt.imread('./jupiter.jpg')
plt.imshow(img)
plt.show()
radius = 12
# with gradient
centers = detectCircles(img.copy(), radius, 1)
print centers
# plot circles
fig = plt.figure()
plt.imshow(img)
circle = []
for center in centers:
    fig.add_subplot(111).add_artist(plt.Circle(center,radius,color=(1,0,0),fill=False))
plt.show()
# without gradient
centers = detectCircles(img.copy(), radius, 0)
print centers
# plot circles
fig = plt.figure()
plt.imshow(img)
circle = []
for center in centers:
    fig.add_subplot(111).add_artist(plt.Circle(center,radius,color=(1,0,0),fill=False))
plt.show()
# extra credit
centers = detectAllCircles(img.copy(), 5, 50)
print centers
# plot circles
fig = plt.figure()
plt.imshow(img)
circle = []
for center in centers:
    fig.add_subplot(111).add_artist(plt.Circle((center[0],center[1]),center[2],color=(1,0,0),fill=False))
plt.show()